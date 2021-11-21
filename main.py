from flask import Flask, render_template

from controllers.postcontroller import PostController
from controllers.projectcontroller import ProjectController
from controllers.socialcontroller import  SocialController

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    social_controller = SocialController
    project_controller = ProjectController

    social =  social_controller.get_social_medias(social_controller)
    project = project_controller.get_projects_to_home(project_controller)

    return render_template('index.html', socials=social, projects=project)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/blog', methods=['GET'])
def blog():

    blog_controller = PostController
    social_controller = SocialController

    blog = blog_controller.get_posts(blog_controller)
    social = social_controller.get_social_medias(social_controller)

    return render_template('blog.html', posts=blog, socials=social)


@app.route('/blog/<int:postid>', methods=['GET'])
def blog_post(postid: int = 1):

    blog_controller = PostController
    project_controller = ProjectController
    social_controller = SocialController

    post = blog_controller.get_post_by_id(blog_controller, postid)
    social = social_controller.get_social_medias(social_controller)

    return render_template('post.html', post=post, socials=social)



@app.route('/projects', methods=['GET'])
def projects():

    project_controller = ProjectController
    social_controller = SocialController

    projects = project_controller.get_projects(project_controller)
    social = social_controller.get_social_medias(social_controller)

    return render_template('projects.html', projects=projects, socials=social)


@app.route('/administracao_do_portifolio', methods=['GET'])
def admin():
    return render_template('admin.html')





if __name__ == '__main__':
    app.run(debug=True)

