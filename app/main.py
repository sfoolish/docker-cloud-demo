import os
import random
import time

from flask import Flask, request, render_template, session, flash, redirect, \
    url_for, jsonify
from flask_restful import Api, Resource


app = Flask(__name__)


class Hello(Resource):
    def get(self):
        return jsonify({'hello': 'docker cloud'})


api = Api(app)
api.add_resource(Hello, "/", endpoint="hello")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
