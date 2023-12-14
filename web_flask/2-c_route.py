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
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
