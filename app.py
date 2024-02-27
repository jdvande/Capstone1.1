from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('Login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
