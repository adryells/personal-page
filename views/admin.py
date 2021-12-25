from flask import (
    Blueprint, render_template
)
bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/', methods=['GET'])
def admin():
    return render_template('admin/admindex.html')


@bp.route('/posts', methods=['GET'])
def admin_posts():
    return render_template('admin/admin_post.html')


@bp.route('/projects', methods=['GET'])
def admin_projects():
    return render_template('admin/admin_project.html')


@bp.route('/social', methods=['GET'])
def admin_social():
    return render_template('admin/admin_social.html')

@bp.route('/colors', methods=['GET'])
def admin_colors():
    return render_template('admin/admin_colors.html')


@bp.route('/home', methods=['GET'])
def admin_home():
    return render_template('admin/admin_home.html')


@bp.route('/data', methods=['GET'])
def admin_data():
    return render_template('admin/admin_gets.html')

