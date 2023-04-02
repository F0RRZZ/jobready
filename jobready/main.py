from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dummy_key'


@app.route('/')
def homepage():
    return render_template('not_auth_homepage.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


def main():
    app.run(port=5000, host='127.0.0.1')


main()
