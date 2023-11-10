#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
-Your web application must be listening on 0.0.0.0, port 5000
-Routes:
--/: display “Hello HBNB!”
--/hbnb: display "HBNB"
--/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space ' ')
--/python/<text>: display “Python ”, followed by the value of the text variable
(replace underscore _ symbols with a space ' ')
---The default value of text is “is cool”
--/number/<n>: display “n is a number” only if n is an integer
--/number_template/<n>: display a HTML page only if n is an integer:
---H1 tag: “Number: n” inside the tag BODY
--/number_odd_or_even/<n>: display a HTML page only if n is an integer:
---H1 tag: “Number: n is even|odd” inside the tag BODY
-You must use the option strict_slashes=False in your route definition
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_(text):
    return f'C {text.replace("_", " ")}'


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text=None):
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n=None):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    if n % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
