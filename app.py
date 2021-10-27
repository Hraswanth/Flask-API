from flask import render_template
from flask import Flask, flash, redirect, request, session, abort, jsonify
from flask_restful import Resource, Api, reqparse, abort
import time
import platform
import platform
import os
from os import getcwd, system
from datetime import datetime

app = Flask(__name__)
api = Api(app)
app.secret_key = os.urandom(100)


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def divide(a, b):
    return a/b


def multiply(a, b):
    return a*b


def powe(a, b):
    return a**b

@app.route('/')
def hello_world():
    return 'Welcome to Calc Flask API'


class HelloWorld(Resource):
    def get(self, value1, value2, calc):
        if calc == "add":
            val = add(int(value1), int(value2))
            return {"Output": val,
                    "Status": "Success"}
        if calc == "subtract":
            val = subtract(int(value1), int(value2))
            return {"Output": val,
                    "Status": "Success"}
        if calc == "divide":
            val = divide(int(value1), int(value2))
            return {"Output": val,
                    "Status": "Success"}
        if calc == "multiply":
            val = multiply(int(value1), int(value2))
            return {"Output": val,
                    "Status": "Success"}
        if calc == "power":
            val = powe(int(value1), int(value2))
            return {"Output": val,
                    "Status": "Success"}


api.add_resource(HelloWorld, "/<string:value1>/<string:value2>/<string:calc>")

if __name__ == '__main__':
    app.run()
