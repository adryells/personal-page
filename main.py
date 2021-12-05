from flask import Flask, render_template, Response

from controllers.postcontroller import PostController
from controllers.projectcontroller import ProjectController
from controllers.socialcontroller import  SocialController
from controllers.tagcontroller import TagController
from models.basemodel import Tag, Config

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():

    social_controller = SocialController
    project_controller = ProjectController

    social = social_controller.get_social_medias(social_controller)
    project = project_controller.get_projects_to_home(project_controller)

    return render_template('index.html', socials=social, projects=project)

@app.errorhandler(404)
def page_not_found(e):
    social_controller = SocialController
    tagcontroller = TagController

    print(tagcontroller.get_tags_from_project(tagcontroller, 1))
    social = social_controller.get_social_medias(social_controller)

    return render_template('404.html', socials=social), 404


@app.errorhandler(500)
def page_not_found_500(e):
    social_controller = SocialController
    social = social_controller.get_social_medias(social_controller)
    return render_template('404.html', socials=social), 500

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
    project_controller = ProjectController
    social_controller = SocialController

    post = blog_controller.get_post_by_id(blog_controller, postid)
    posts = blog_controller.get_posts(blog_controller)
    social = social_controller.get_social_medias(social_controller)
    projects = project_controller.get_projects_to_home(project_controller)

    if not post:
        return render_template('404.html'), 404

    return render_template('post.html', post=post, posts=posts, socials=social, projects=projects)


@app.route('/projects', methods=['GET'])
@app.route('/projects/<orderby>', methods=['GET'])
def projects(orderby:str = "recent"):

    project_controller = ProjectController
    social_controller = SocialController

    projects = project_controller.get_projects(project_controller, orderby)
    social = social_controller.get_social_medias(social_controller)

    return render_template('projects.html', projects=projects, socials=social)


@app.route('/paymeacoffee', methods=['GET'])
def pay_me_a_coffee():
    social_controller = SocialController
    social = social_controller.get_social_medias(social_controller)

    return render_template('paymeacoffee.html', socials=social)


@app.route('/administracao_do_portifolio', methods=['GET'])
def admin():
    return render_template('admin.html')





if __name__ == '__main__':
    app.run(debug=True)

