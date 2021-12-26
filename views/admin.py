from flask import (
    Blueprint, render_template, request
)
from werkzeug.utils import redirect

from controllers.admincontroller import AdminController
from controllers.postcontroller import PostController
from controllers.projectcontroller import ProjectController
from controllers.socialcontroller import SocialController
from controllers.tagcontroller import TagController

bp = Blueprint('admin', __name__, url_prefix='/admin')

admincontroller = AdminController
postcontroller = PostController
projectcontroller = ProjectController
socialcontroller = SocialController
tagcontroller = TagController


@bp.route('/login', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
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
    posts = postcontroller.get_posts(postcontroller)
    return render_template('admin/admin_post.html', posts=posts)

@bp.route('/posts/addpost', methods=['POST'])
def admin_add_post():
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

    return redirect("admin_posts")

@bp.route('/posts/updatepost', methods=['POST', 'PUT'])
def admin_update_post():
    if request.method == "POST":
        postcontroller.update_post(
            self=postcontroller,
            postid=request.form['postid'],
            changes=request.form
        )

    return redirect("admin_posts")


@bp.route('/projects', methods=['GET'])
def admin_projects():
    projects = projectcontroller.get_projects(projectcontroller, "recent")
    return render_template('admin/admin_project.html', projects=projects)


@bp.route('/projects/addproject', methods=['POST'])
def admin_add_project():
    if request.method == "POST":
        projectcontroller.add_project(
            self=postcontroller,
            title=request.form['title'],
            shortdescription=request.form['short'],
            bigdescription=request.form['big'],
            active=bool(int(request.form['active'])),
            media=request.form['media'],
            link=request.form['link']
        )

    return redirect("/admin/projects")

@bp.route('/projects/updateproject', methods=['POST', 'PUT'])
def admin_update_project():
    if request.method == "POST":
        projectcontroller.update_project(
            self=postcontroller,
            projectid=request.form['projectid'],
            changes=request.form
        )

    return redirect("/admin/projects")


@bp.route('/social', methods=['GET'])
def admin_social():
    socials = socialcontroller.get_social_medias(socialcontroller)
    return render_template('admin/admin_social.html', socials=socials)


@bp.route('/social/addsocial', methods=['PUT', 'POST'])
def admin_add_social():
    socialcontroller.add_social(
        self=socialcontroller,
        active=bool(request.form['active']),
        media=request.form['media'],
        link=request.form['link'],
        name=request.form['name']
    )

    return redirect("/admin/social")


@bp.route('/social/updatesocial', methods=['PUT', 'POST'])
def admin_update_social():
    socialcontroller.update_social(
        self=socialcontroller,
        changes=request.form,
        socialid=request.form['socialid']
    )

    return redirect("/admin/social")


@bp.route('/colors', methods=['GET'])
def admin_colors():
    return render_template('admin/admin_colors.html')


@bp.route('/home', methods=['GET'])
def admin_home():
    return render_template('admin/admin_home.html')


@bp.route('/data', methods=['GET'])
def admin_data():
    posts = postcontroller.get_posts(postcontroller, "recent")
    projects = projectcontroller.get_projects(projectcontroller, "recent")
    socials = socialcontroller.get_social_medias(socialcontroller)
    tags = tagcontroller.get_tags(tagcontroller)

    return render_template('admin/admin_gets.html', posts=posts, projects=projects, socials=socials, tags=tags)

