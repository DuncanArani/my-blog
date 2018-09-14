
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    vote=RadioField('default field arguments', choices=[('1', 'like'), ('1', 'dislike')])
    submit = SubmitField('SUBMIT')  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit') 

class blogForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'Interview'), ('2', 'Pick Up Lines'), ('3', 'Promotion'),('4','Product')])
    content = TextAreaField('YOUR blog')
    submit = SubmitField('Create blog')

class likeForm(FlaskForm):
    '''
    Class to create a wtf form for likeing a blog
    '''
    submit = SubmitField('like')