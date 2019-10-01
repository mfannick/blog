from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_quote
from ..models import User,Blog,Comment,Subscribe
from .. import db,photos
from .forms import UpdateProfile,BlogForm,CommentForm,UpdateblogForm,SubscribeForm
from flask_login import login_required,current_user
import datetime
from ..email import mail_subscribemessage

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    blogs=Blog.query.all()
    quote=get_quote()
    title = 'Home - Welcome to Bloging website'
    return render_template('index.html',title = title,blogs=blogs,quote=quote)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    blog=Blog.query.filter_by(userId=current_user.id).all()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user,blogWrite=blog)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form = form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def newBlog():
    form = BlogForm()
    if form.validate_on_submit():
        blogTitle = form.blogTitle.data
        blogWrite = form.blogWrite.data
        newBlog = Blog(blogTitle=blogTitle,blogWrite=blogWrite,userId=current_user._get_current_object().id)
        # newBlog.saveBlog()
        db.session.add(newBlog)
        db.session.commit()
        return redirect(url_for('.index'))
    title = 'New blog'
    return render_template('newBlog.html',title = title,blog_form=form)





@main.route('/comment/blog/<int:id>', methods = ['GET','POST'])
@login_required
def commentBlog(id):
    blog=Blog.query.filter_by(id=id).first()
    if blog is None:
        abort(404)
    form = CommentForm()
    title='comment'
    if form.validate_on_submit():
        commentWrite= form.commentWrite.data
        newComment=Comment(commentWrite=commentWrite,blog=blog,userId=current_user._get_current_object().id)
        newComment.saveComment()
        return redirect(url_for('.seeCommentBlog',id=blog.id))

    return render_template('comment.html',comment_form = form,title=title)


@main.route('/viewcomment/blog/<int:id>', methods = ['GET','POST'])
def seeCommentBlog(id):
    quote=get_quote()
    user=User.query.filter_by(id=id).first()
    blog=Blog.query.filter_by(id=id).first()
    comments=Comment.query.filter_by(blogId=id)
    return render_template('index.html',blog=blog,comments=comments,user=user,quote=quote)

@main.route('/deleteblog/blog/<int:id>', methods = ['GET','POST'])
@login_required
def deleteBlog(id):
    user=User.query.filter_by(id=id).first()
    blog=Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('.index'))

    return render_template('index.html',blog=blog,user=user)


@main.route('/blog/<int:blogId>/update',methods = ['GET','POST'])
@login_required
def updateBlog(blogId):
    blog=Blog.query.get(blogId)
    form = UpdateblogForm()
    if form.validate_on_submit():
        blog.blogWrite = form.blogWrite.data
        blog.blogTitle=form.blogTitle.data
        db.session.commit()
        return redirect(url_for('.index'))
    return render_template('updateBlog.html',updateblog_form = form)

@main.route('/subscribe/blogsite/', methods = ['GET','POST'])
def subscribeBlog():
    form = SubscribeForm()
    title='subscribe'
    if form.validate_on_submit():
        subscriberName= form.subscriberName.data
        subscriberEmail= form.subscriberEmail.data
        newSubscriber=Subscribe(subscriberName=subscriberName,subscriberEmail=subscriberEmail)
        db.session.add(newSubscriber)
        db.session.commit()
        mail_subscribemessage("Thank you for the subscription","email/welcome_subscriber",newSubscriber.subscriberEmail,newSubscriber=newSubscriber)
        return redirect(url_for('.index'))

    return render_template('subscribe.html',subscribe_form = form,title=title)





    