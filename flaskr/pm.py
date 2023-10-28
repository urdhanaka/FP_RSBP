from flask import (
    Blueprint, render_template
)

bp = Blueprint('root', __name__)

@bp.route('/', methods = ['GET', 'POST'])
def root():
    return render_template('root.html')

