#!/usr/bin/python3
""" Hello world with flask """

from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
