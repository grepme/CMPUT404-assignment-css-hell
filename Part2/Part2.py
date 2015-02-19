from flask import Flask
from flask import render_template
from flask import send_from_directory

import os

app = Flask(__name__)


@app.route('/')
def index():
    return "You probably want /good or /bad"


# Taken from http://flask.pocoo.org/docs/0.10/patterns/favicon/
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/good')
def good():
    return render_template('index.html', css_file="good")


@app.route('/bad')
def bad():
    return render_template('index.html', css_file="bad")


if __name__ == '__main__':
    app.run()
