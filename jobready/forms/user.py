from flask_wtf import FlaskForm
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
