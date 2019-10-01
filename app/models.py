from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index =True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(5000))
    profile_pic_path = db.Column(db.String)
    pass_secure = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    commentId = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    blogTitle = db.Column(db.String)
    blogWrite = db.Column(db.String(1000))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    userId = db.Column(db.Integer,db.ForeignKey("users.id"))
    commentId = db.relationship('Comment',backref =  'blog',lazy = "dynamic")

    # def saveBlog(self):
    #     db.session.add(self)
    #     db.session.commit()

    @classmethod
    def getBlogs(cls,id):
        blogs = Blog.query.filter_by(userId=id).all()
        return blogs

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    commentWrite = db.Column(db.String(1000))
    timeComment = db.Column(db.DateTime,default=datetime.utcnow)
    userId= db.Column(db.Integer,db.ForeignKey("users.id"))
    blogId = db.Column(db.Integer,db.ForeignKey("blogs.id"))

    def saveComment(self):
        db.session.add(self)
        db.session.commit()

    
    @classmethod
    def getComment(cls,id):
        comments = Comment.query.filter_by(blogId=id).all()
        return comments

class Subscribe(db.Model):
    __tablename__='subscribes'

    id=db.Column(db.Integer,primary_key=True)
    subscriberName=db.Column(db.String(255))
    subscriberEmail=db.Column(db.String(255),unique = True,index = True, nullable=False)

class Quotes:
    '''
    Quote class to define Movie Objects
    '''

    def __init__(self,id,author,content):
        self.id =id
        self.author = author
        self.content = content
     


 

