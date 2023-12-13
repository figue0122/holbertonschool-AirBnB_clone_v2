#!/usr/bin/python3
""" Hello world with flask """

from flask import Flask
""" Flask class """
app = Flask(__name__)
""" Flask object """
@app.route('/', strict_slashes=False)

def hello_hbnb():
    """ Hello world with flask """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
