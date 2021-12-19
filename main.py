from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from controllers.projectcontroller import ProjectController
from controllers.postcontroller import PostController
from controllers.socialcontroller import SocialController

from models.basemodel import Tag, Config


app = Flask(__name__)


######################
###### MAIN PAGE #####
######################

blog_controller = PostController
social_controller = SocialController
project_controller = ProjectController


@app.route('/', methods=['GET'])
def index():

    social = social_controller.get_social_medias(social_controller)
    project = project_controller.get_projects_to_home(project_controller)

    return render_template('index.html', socials=social, projects=project)


######################
###### ADMIN #########
######################


@app.route('/administracao_do_portifolio', methods=['GET'])
def admin():
    return render_template('admin/admindex.html')


@app.route('/administracao_do_portifolio/posts', methods=['GET'])
def admin_posts():
    return render_template('admin/admin_post.html')


@app.route('/administracao_do_portifolio/projects', methods=['GET'])
def admin_projects():
    return render_template('admin/admin_project.html')


@app.route('/administracao_do_portifolio/social', methods=['GET'])
def admin_social():
    return render_template('admin/admin_social.html')

@app.route('/administracao_do_portifolio/colors', methods=['GET'])
def admin_colors():
    return render_template('admin/admin_colors.html')


@app.route('/administracao_do_portifolio/home', methods=['GET'])
def admin_home():
    return render_template('admin/admin_home.html')


@app.route('/administracao_do_portifolio/data', methods=['GET'])
def admin_data():
    return render_template('admin/admin_gets.html')


######################
###### BLOG ##########
######################

@app.route('/blog', methods=['GET'])
@app.route('/blog/<orderby>', methods=['GET'])
def blog(orderby:str="recent"):
    blog = blog_controller.get_posts(blog_controller, orderby)
    social = social_controller.get_social_medias(social_controller)

    return render_template('blog.html', posts=blog, socials=social)

@app.route('/blog/<int:postid>', methods=['GET'])
def blog_post(postid: int = 1):
    post = blog_controller.get_post_by_id(blog_controller, postid)
    social = social_controller.get_social_medias(social_controller)

    if not post:
        return render_template('404.html'), 404

    return render_template('post.html', post=post, socials=social, comments=post.comments)


##########################
###### PROJECTS ##########
##########################

@app.route('/projects', methods=['GET'])
@app.route('/projects/<orderby>', methods=['GET'])
def projects(orderby:str = "recent"):
    projects = project_controller.get_projects(project_controller, orderby)
    social = social_controller.get_social_medias(social_controller)

    return render_template('projects.html', projects=projects, socials=social)


##########################
###### PAYMEACOFFEE ######
##########################


@app.route('/paymeacoffee', methods=['GET'])
def pay_me_a_coffee():
    social = social_controller.get_social_medias(social_controller)

    return render_template('paymeacoffee.html', socials=social)


##########################
###### ERRORS ############
##########################

@app.errorhandler(404)
def page_not_found(e):
    social = social_controller.get_social_medias(social_controller)

    return render_template('errors/404.html', socials=social), 404


@app.errorhandler(500)
def page_not_found_500(e):
    social = social_controller.get_social_medias(social_controller)

    return render_template('errors/404.html', socials=social), 500


if __name__ == '__main__':
    app.run(debug=True)

