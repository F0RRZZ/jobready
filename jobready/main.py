import os

from flask import Flask, redirect, render_template, request
import flask_login
from flask_restful import Api
from werkzeug.utils import secure_filename

from data import db_session
from data.users import User
from data.templates import Template
from data.resumes import Resume
from data.users_resource import UsersResource, UsersListResource
from forms.user import RegisterForm, LoginForm, ProfileForm

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'dummy_key'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def homepage():
    if flask_login.current_user.is_authenticated:
        return redirect('/templates')
    return render_template('homepage.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = (
            db_sess.query(User).filter(User.email == form.email.data).first()
        )
        if user and user.check_password(form.password.data):
            flask_login.login_user(user, remember=True)
            return redirect('/')
        return render_template(
            'login.html', message='Wrong login or password', form=form
        )
    return render_template('login.html', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_confirm.data:
            return render_template(
                'registration.html',
                message="Passwords don't match",
                form=form,
            )
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template(
                'registration.html',
                message='Email is already exists',
                form=form,
            )
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('registration.html', form=form)


@app.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return redirect('/')


@app.route('/profile/<int:user_id>', methods=['GET', 'POST'])
def profile(user_id):
    form = ProfileForm()
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if form.validate_on_submit() and request.method == 'POST':
        avatar = form.avatar.data
        if avatar:
            filename = secure_filename(avatar.filename)
            avatar_path = os.path.join(
                'static\\img\\avatars', f'{user.id}.{filename.split(".")[-1]}'
            )
            avatar.save(avatar_path)
        else:
            avatar_path = user.avatar
        user.username = form.username.data
        user.email = form.email.data
        user.bio = form.bio.data
        user.avatar = avatar_path
        db_sess.commit()
    return render_template('profile.html', form=form, user=user)


@app.route('/resume/create/<int:template_id>', methods=['GET', 'POST'])
@flask_login.login_required
def create_resume(template_id):
    db_sess = db_session.create_session()
    template_file = db_sess.query(Template).get(template_id)
    return render_template(template_file.template_path)


@app.route('/resume/edit/<int:resume_id>', methods=['GET', 'POST'])
@flask_login.login_required
def edit_resume(resume_id):
    return render_template('resume_edit.html')


@app.route('/templates', methods=['GET'])
@flask_login.login_required
def templates():
    db_sess = db_session.create_session()
    templates_list = db_sess.query(Template).all()
    return render_template('templates.html', templates_list=templates_list)


@app.route('/help')
@flask_login.login_required
def help_():
    return render_template('help.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/help')
def help_e():
    return render_template('help.html', title='Help')


def main():
    db_session.global_init('db/database.db')
    api.add_resource(UsersResource, '/api/users/<int:user_id>')
    api.add_resource(UsersListResource, '/api/users')
    app.run(port=5000, host='127.0.0.1')


main()
