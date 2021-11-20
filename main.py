from flask import Flask, render_template

from controllers.postcontroller import PostController
from controllers.projectcontroller import ProjectController
from controllers.socialcontroller import  SocialController

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    social_controller = SocialController

    social =  social_controller.get_social_medias(social_controller)

    return render_template('index.html', socials=social)



@app.route('/blog', methods=['GET'])
def blog():

    blog_controller = PostController
    social_controller = SocialController

    blog = blog_controller.get_posts(blog_controller)
    social = social_controller.get_social_medias(social_controller)

    return render_template('blog.html', blogs=blog, socials=social)


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

