from flask import render_template, jsonify, Blueprint
from flask_login import current_user


admin_bp = Blueprint('admin', __name__)