from flask_restx import Api
from app.apis.hello_world import hello

api = Api(
    title="Playground",
    version=1.0,
    description="Description of api"
)

api.add_namespace(hello, path='/')