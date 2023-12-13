#!/usr/bin/python3
""" Hello world with flask """
from flask import Flask
""" Flask class """
app = Flask(__name__)
""" Flask object """
app.url_map.strict_slashes = False

""" Route decorator """

app.route('/')
def hello():
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
