from flask import Flask
from src.routes import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")
