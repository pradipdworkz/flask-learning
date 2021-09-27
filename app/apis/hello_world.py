from flask import jsonify
from flask_restx import Resource, Namespace, fields
from app.extension import api


hello = Namespace('Hello to the World')


# helloModel = hello.model('Hello', {
#     'status': fields.String(required=True, description='Default status'),
#     'value': fields.String(required=True, description='Default status')
# })

@hello.route('')
class Hello(Resource):
    # @api.marshal_list_with(helloModel)
    def get(self):
        return jsonify({'status': 'SUCCESSFUL', 'value': 'Hello World'}), 200