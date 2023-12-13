#!/usr/bin/python3
""" Hello world with flask """

from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Hello world with flask """
    return 'Hello HBNB!'
