from flask import (
    Blueprint, render_template
)
bp = Blueprint('auth', __name__, url_prefix='/admin')

@bp.route('/administracao_do_portifolio', methods=['GET'])
def admin():
    return render_template('admin/admindex.html')


@bp.route('/administracao_do_portifolio/posts', methods=['GET'])
def admin_posts():
    return render_template('admin/admin_post.html')


@bp.route('/administracao_do_portifolio/projects', methods=['GET'])
def admin_projects():
    return render_template('admin/admin_project.html')


@bp.route('/administracao_do_portifolio/social', methods=['GET'])
def admin_social():
    return render_template('admin/admin_social.html')

@bp.route('/administracao_do_portifolio/colors', methods=['GET'])
def admin_colors():
    return render_template('admin/admin_colors.html')


@bp.route('/administracao_do_portifolio/home', methods=['GET'])
def admin_home():
    return render_template('admin/admin_home.html')


@bp.route('/administracao_do_portifolio/data', methods=['GET'])
def admin_data():
    return render_template('admin/admin_gets.html')

