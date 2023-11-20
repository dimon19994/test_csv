from app import app
from .data import data


app.register_blueprint(data)
