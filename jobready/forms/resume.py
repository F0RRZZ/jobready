from flask_wtf import FlaskForm, file
import wtforms


class ResumeForm(FlaskForm):
    name = wtforms.StringField('Name')
    image = wtforms.FileField(
        'Image',
        validators=[file.FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')],
    )
    position = wtforms.StringField('Position')
    email = wtforms.EmailField('Email')
    bio = wtforms.TextAreaField('Bio')
    place_of_residence = wtforms.StringField('Place of residence')
    skills = wtforms.TextAreaField('Skills')
    experience = wtforms.TextAreaField('Experience')
    education = wtforms.TextAreaField('Education')
    achievments = wtforms.TextAreaField('Achievments')
    contacts = wtforms.TextAreaField('Contacts')
