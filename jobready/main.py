from flask import Flask, redirect, render_template
import flask_login

from data import db_session
from data.users import User
from forms.user import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dummy_key'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


@app.route('/')
def homepage():
    return render_template('not_auth_homepage.html')


@app.route('/about')
def about():
    return render_template('about.html', title='JobReady | About')


@app.route('/help')
def help_e():
    return render_template('help.html', title='JobReady | Help')


def main():
    db_session.global_init('db/database.db')
    app.run(port=5000, host='127.0.0.1')


main()
