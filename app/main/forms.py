from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Email
from wtforms import ValidationError
from ..models import Subscribe

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    

class BlogForm(FlaskForm):
    blogTitle= StringField('Your blog title',validators=[Required()])
    blogWrite=  TextAreaField('Write your blog',validators =[Required()])
    submitBlog= SubmitField('Submit')
class UpdateblogForm(FlaskForm):
    blogTitle= StringField('Your updated blog title',validators=[Required()])
    blogWrite=  TextAreaField('Write updated your blog',validators =[Required()])
    submitBlog= SubmitField('updateBlog')
class CommentForm(FlaskForm):
	commentWrite = TextAreaField('Add comment',validators=[Required()])
	submitComment = SubmitField('comment')

class SubscribeForm(FlaskForm):
    subscriberName= StringField('Enter your name',validators = [Required()])
    subscriberEmail = StringField('Your Email Address',validators=[Required(),Email()])
    submit = SubmitField('Subscribe')
    def validate_subscriberEmail(self,data_field):
        if Subscribe.query.filter_by(subscriberEmail =data_field.data).first():
            raise ValidationError('There is an account with that subscriberEmail')

    def validate_subscriberName(self,data_field):
        if Subscribe.query.filter_by(subscriberName = data_field.data).first():
            raise ValidationError('That subscriberName is taken')