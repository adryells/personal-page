from flask import (
    Blueprint, render_template, request
)

from controllers.admincontroller import AdminController
from controllers.postcontroller import PostController
from controllers.projectcontroller import ProjectController
from controllers.socialcontroller import SocialController
from controllers.tagcontroller import TagController
from models.basemodel import Config

bp = Blueprint('admin', __name__, url_prefix='/admin')

admincontroller = AdminController
postcontroller = PostController
projectcontroller = ProjectController
socialcontroller = SocialController
tagcontroller = TagController

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        user_password = request.form['password']
        admin_is_ok = admincontroller.validate_admin_exists(admincontroller, user_name, user_password)

        if admin_is_ok:
            return render_template('admin/admindex.html')

    return render_template("admin/login.html")


@bp.route('/posts', methods=['GET', 'POST', 'PUT'])
@bp.route('/posts/<orderby>', methods=['GET'])
def admin_posts(orderby: str = "recent"):
    session = Config.session
    if request.method == "POST":
        postcontroller.add_post(
            self=postcontroller,
            title=request.form['title'],
            description=request.form['description'],
            content=request.form['content'],
            media=request.form['media'],
            active=bool(request.form['active']),
            tags=request.form['tags']
        )

    if request.method == "PUT":
        postcontroller.update_post(
            postcontroller,
            request.form['postid'],
            changes=request.form['changes']
        )

    session.commit()
    posts = postcontroller.get_posts(postcontroller)
    return render_template('admin/admin_post.html', posts=posts)


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

