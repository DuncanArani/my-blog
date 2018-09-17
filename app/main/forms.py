
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'Like'), ('1', 'DisLike')])
    submit = SubmitField('SUBMIT')  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit') 

class BlogForm(FlaskForm):
    User_id = SelectField('Select user', choices=[('1', 'my blog')])
    content = TextAreaField('MY BLOG')
    submit = SubmitField('Create blog')

class LikeForm(FlaskForm):
    '''
    Class to create a wtf form for liking a blog
    '''
    submit = SubmitField('Like')