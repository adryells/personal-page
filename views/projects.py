from flask import (
    Blueprint, render_template
)

from controllers.projectcontroller import ProjectController
from controllers.socialcontroller import SocialController

social_controller = SocialController
project_controller = ProjectController


bp = Blueprint('projects', __name__, url_prefix='/projects')
@bp.route('/', methods=['GET'])
@bp.route('/<orderby>', methods=['GET'])
def projects(orderby:str = "recent"):
    allprojects = project_controller.get_projects(project_controller, orderby)
    social = social_controller.get_social_medias(social_controller)

    return render_template('projects.html', projects=allprojects, socials=social)