from flask import Blueprint, render_template

from controllers.postcontroller import PostController
from controllers.socialcontroller import SocialController

blog_controller = PostController
social_controller = SocialController

bp = Blueprint('blog', __name__, url_prefix='/blog')


@bp.route('/', methods=['GET'])
@bp.route('/<orderby>', methods=['GET'])
def blog(orderby:str="recent"):
    blog = blog_controller.get_posts(blog_controller, orderby)
    social = social_controller.get_social_medias(social_controller)

    return render_template('blog.html', posts=blog, socials=social)

@bp.route('/<int:postid>', methods=['GET'])
def blog_post(postid: int = 1):
    post = blog_controller.get_post_by_id(blog_controller, postid)
    social = social_controller.get_social_medias(social_controller)

    if not post:
        return render_template('404.html'), 404

    return render_template('post.html', post=post, socials=social)