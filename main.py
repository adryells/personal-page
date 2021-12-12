from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from controllers.commentcontroller import CommentController
from controllers.projectcontroller import ProjectController
from controllers.postcontroller import PostController
from controllers.socialcontroller import SocialController

from models.basemodel import Tag, Config


app = Flask(__name__)


######################
###### MAIN PAGE #####
######################


@app.route('/', methods=['GET'])
def index():

    social_controller = SocialController
    project_controller = ProjectController

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

    blog_controller = PostController
    social_controller = SocialController

    blog = blog_controller.get_posts(blog_controller, orderby)
    social = social_controller.get_social_medias(social_controller)

    return render_template('blog.html', posts=blog, socials=social)

@app.route('/blog/add', methods=['GET', 'POST'])
def add_post():

    blog_controller = PostController

    post = blog_controller.add_post(blog_controller,
                                    title="ue",
                                    active=True,
                                    content="kkkkk",
                                    description="kkkk",
                                    media="media",
                                    tags=[1,2,3]
                                    )
    return "Post adicionado"

@app.route('/blog/update/<int:postid>', methods=['GET', 'PUT'])
def update_post(postid:int):
    session = Config.session

    blog_controller = PostController

    tags = [session.query(Tag).filter(Tag.tagid == tagid).one() for tagid in [5,6,4]]
    blog_controller.update_post(blog_controller,postid,{"title":"mentira sio", "active":False, "content":"jjjj", "description":"lllllqdqidhwpowpowpgobwgpwbpbpwopw<br>jlsbblaiviviebwiviwwkwbvkwwebeeheeheh<br>jlslslkvllsvslslslsslvvvv<br>", "media":"kkskksks", "tags":tags})

    return f"Post {postid} atualizado"



@app.route('/blog/<int:postid>', methods=['GET'])
def blog_post(postid: int = 1):


    blog_controller = PostController
    social_controller = SocialController

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

    project_controller = ProjectController
    social_controller = SocialController

    projects = project_controller.get_projects(project_controller, orderby)
    social = social_controller.get_social_medias(social_controller)

    return render_template('projects.html', projects=projects, socials=social)


##########################
###### PAYMEACOFFEE ######
##########################


@app.route('/paymeacoffee', methods=['GET'])
def pay_me_a_coffee():
    social_controller = SocialController
    social = social_controller.get_social_medias(social_controller)

    return render_template('paymeacoffee.html', socials=social)

##########################
###### COMMENTS###########
##########################
@app.route('/blog/<int:postid>/addcomment', methods=['POST'])
def addcomment(postid):

    if request.method == 'POST':
        commenter = request.form['nickname']
        content = request.form['content']

        comment_controller = CommentController
        comment_controller.add_comment(comment_controller, commenter, content, postid)
        return redirect(url_for('blog_post', postid=postid))
        # return f"Comment: {comment.commentid} adicionado no post: {postid}"


##########################
###### COMMENTS###########
##########################
@app.route('/blog/<int:postid>/addlike', methods=['POST'])
def addlike(postid):

    if request.method == 'POST':

        post_controller = PostController
        post_controller.add_like_to_post(post_controller, postid)
        return redirect(url_for('blog_post', postid=postid))


##########################
###### ERRORS ############
##########################

@app.errorhandler(404)
def page_not_found(e):
    social_controller = SocialController

    social = social_controller.get_social_medias(social_controller)

    return render_template('404.html', socials=social), 404


@app.errorhandler(500)
def page_not_found_500(e):
    social_controller = SocialController
    social = social_controller.get_social_medias(social_controller)
    return render_template('404.html', socials=social), 500


if __name__ == '__main__':
    app.run(debug=True)

