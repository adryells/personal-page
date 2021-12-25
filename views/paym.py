from flask import (
    Blueprint, render_template
)

from controllers.socialcontroller import SocialController

social_controller = SocialController

bp = Blueprint('payme', __name__, url_prefix='/')

@bp.route('/paymeacoffee', methods=['GET'])
def pay_me_a_coffee():
    social = social_controller.get_social_medias(social_controller)

    return render_template('paymeacoffee.html', socials=social)