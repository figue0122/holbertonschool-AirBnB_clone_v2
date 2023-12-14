#!/usr/bin/python3
""" Hello world with flask """

from flask import Flask
from flask import render_template
""" Importing flask and render_template """

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Hello world with flask """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Hello world with flask """
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """ Hello world with flask """
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text='is cool'):
    """ Hello world with flask """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def number(n):
    """ Hello world with flask """
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Hello world with flask """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
