from flask import Flask, render_template

from controllers.homecontentcontroller import HomeContentController
from controllers.projectcontroller import ProjectController
from controllers.postcontroller import PostController
from controllers.socialcontroller import SocialController

from views import admin, errors, paym, blog, projects

app = Flask(__name__)


######################
###### MAIN PAGE #####
######################

social_controller = SocialController
project_controller = ProjectController
hc_controller = HomeContentController


@app.route('/', methods=['GET'])
def index():

    social = social_controller.get_social_medias(social_controller)
    project = project_controller.get_projects_to_home(project_controller)
    whatido = hc_controller.get_actual_what_i_do(hc_controller)
    whoiam = hc_controller.get_actual_who_i_am(hc_controller)

    return render_template('index.html', socials=social, projects=project, whatido=whatido, whoiam=whoiam)


if __name__ == '__main__':
    app.register_blueprint(admin.bp)
    app.register_blueprint(errors.bp)
    app.register_blueprint(paym.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(projects.bp)
    app.run(debug=True)

