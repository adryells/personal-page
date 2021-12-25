from flask import (
    Blueprint, render_template
)

from controllers.socialcontroller import SocialController

bp = Blueprint('error', __name__, url_prefix='/error')
social_controller = SocialController

@bp.errorhandler(404)
def page_not_found(e):
    social = social_controller.get_social_medias(social_controller)

    return render_template('errors/404.html', socials=social), 404


@bp.errorhandler(500)
def page_not_found_500(e):
    social = social_controller.get_social_medias(social_controller)

    return render_template('errors/404.html', socials=social), 500