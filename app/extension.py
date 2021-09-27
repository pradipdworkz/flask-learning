from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

db = SQLAlchemy()

api = Api(
    title="Playground",
    version=1.0,
    description="Description of api"
)