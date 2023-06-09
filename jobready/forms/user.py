from flask_wtf import FlaskForm, file
import wtforms
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = wtforms.EmailField('Email', validators=[DataRequired()])
    password = wtforms.PasswordField('Password', validators=[DataRequired()])
    password_confirm = wtforms.PasswordField(
        'Password Confirm', validators=[DataRequired()]
    )
    username = wtforms.StringField('Username', validators=[DataRequired()])
    submit = wtforms.SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = wtforms.EmailField('Email', validators=[DataRequired()])
    password = wtforms.PasswordField('Password', validators=[DataRequired()])
    submit = wtforms.SubmitField('Sign up')


class ProfileForm(FlaskForm):
    avatar = wtforms.FileField(
        'Image',
        validators=[file.FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')],
    )
    username = wtforms.StringField('Username', validators=[DataRequired()])
    email = wtforms.EmailField('Email', validators=[DataRequired()])
    bio = wtforms.TextAreaField('Bio')
    submit = wtforms.SubmitField('Accept changes')
