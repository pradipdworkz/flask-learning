import os
from flask import Flask
from app.extension import db, api
from app.apis.hello_world import hello

api.add_namespace(hello, path='')

PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split("/")[-1]

def create_app(app_name=PKG_NAME):
    app = Flask(__name__)
    db.init_app(app)
    with app.app_context():
        api.init_app(app)
    return app