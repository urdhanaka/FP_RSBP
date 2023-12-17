from flask import Blueprint
from src.controller.regex_controller import regex
from src.controller.naive_controller import naive

api = Blueprint("api", __name__)
api.register_blueprint(regex, url_prefix="/regex")
api.register_blueprint(naive, url_prefix="/naive")
