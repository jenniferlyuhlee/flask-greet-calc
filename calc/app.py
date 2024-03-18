# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request
 
app = Flask(__name__)

@app.route('/add')
def handle_add():
    """add a and b query parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a, b))

@app.route('/sub')
def handle_sub():
    """subtract a and b query parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a, b))

@app.route('/mult')
def handle_mult():
    """multiply a and b query parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a, b))

@app.route('/div')
def handle_div():
    """divide a and b query parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a, b))


# Further study
operators = {
    "add": add,
    "sub":sub,
    "mult": mult,
    "div":div
}

@app.route('/math/<operator>')
def math_function(operator):
    """does math function on a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operators[operator](a, b)
    return str(result)
