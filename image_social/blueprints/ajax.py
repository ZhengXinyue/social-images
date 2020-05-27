from flask import render_template, jsonify, Blueprint
from flask_login import current_user


ajax_bp = Blueprint('ajax', __name__)