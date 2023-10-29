from flask import Blueprint
from src.controller.regex_controller import regex

api = Blueprint('api', __name__)

api.register_blueprint(regex, url_prefix="/regex")
