from flask import Blueprint

from src.controller.regex_controller import regex
from src.controller.naive_controller import naive
from src.controller.kmp_controller import kmp
from src.controller.z_controller import z
from src.controller.boyer_moore_controller import boyer_moore
from src.controller.evaluation_controller import eval_func

api = Blueprint("api", __name__)
api.register_blueprint(regex, url_prefix="/regex")
api.register_blueprint(naive, url_prefix="/naive")
api.register_blueprint(kmp, url_prefix="/kmp")
api.register_blueprint(z, url_prefix="/z")
api.register_blueprint(boyer_moore, url_prefix="/boyer_moore")
api.register_blueprint(eval_func, url_prefix="/evaluation")
