from flask import Flask

app = Flask(__name__)

from src.routes import api
app.register_blueprint(api, url_prefix="/api")
