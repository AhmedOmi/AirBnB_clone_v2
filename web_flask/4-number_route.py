#!/usr/bin/python3

from flask import Flask, escape, request, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def var(text):
    return "C " + text


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def setted(text="is cool"):
    text = text.replace("_", " ")
    return ('Python ' + text)


@app.route("/number/<n>")
def integer(n):
    try:
        int(n)
        return (n + ' is a number')
    except:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
