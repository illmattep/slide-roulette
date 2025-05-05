from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])

class ImageForm(FlaskForm):
    image = FileField('Image', validators=[DataRequired()])
    submit = SubmitField('Add Image')

class WordForm(FlaskForm):
    word = StringField('Word', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Add Word')

class SettingsForm(FlaskForm):
    setting_name = StringField('Setting Name', validators=[DataRequired()])
    setting_value = StringField('Setting Value', validators=[DataRequired()])
    submit = SubmitField('Update Settings')