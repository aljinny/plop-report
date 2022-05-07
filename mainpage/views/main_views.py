from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

from mainpage.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/plop_m')
def index():
    return redirect(url_for('question._list'))


