from flask import jsonify
from flask_restx import Resource, Namespace, fields

hello = Namespace('Hello to the World')

helloModel = hello.model('Hello', {
    'status': fields.String(required=True, description='Default status'),
    'value': fields.String(required=True, description='Default status')
})

@hello.route('hello')
class Hello(Resource):
    def get(self):
        return {'status': 'SUCCESSFUL', 'value': 'Hello World'}