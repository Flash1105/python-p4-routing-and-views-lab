#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(f"Received parameter: {parameter}")
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(map(str, range(parameter)))

@app.route('/math/<int:param1>/<operation>/<int:param2>')
def math(param1, operation, param2):
    if operation == '+':
        result = param1 + param2
    elif operation == '-':
        result = param1 - param2
    elif operation == '*':
        result = param1 * param2
    elif operation == 'div':
        if param2 != 0:
            result = param1 / param2
        else:
            result = "Division by zero"
    elif operation == '%':
        if param2 != 0:
            result = param1 % param2
        else:
            result = "Modulo by zero"
    else:
        result = "Invalid operation"
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
