from flask import Flask, render_template, jsonify
from controllers.projectcontroller import ProjectController
from controllers import postcontroller, projectcontroller, socialcontroller, technologycontroller

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    controller = ProjectController
    projects = controller.get_projects(controller)
    return render_template('index.html', projects=projects)


if __name__ == '__main__':
    app.run(debug=False)

