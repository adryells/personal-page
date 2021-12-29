from random import choice

from models.basemodel import Config, Project
from sqlalchemy import select

class ProjectController:

    def add_project(self, title: str, shortdescription: str, bigdescription: str,  media: str, link: str, active: bool) -> Project:
        session = Config.session

        new_project = Project(
            title=title,
            shortdescription=shortdescription,
            bigdescription=bigdescription,
            link=link,
            media=media,
            active=active
        )

        session.add(new_project)
        session.commit()

        return new_project

    def update_project(self, projectid: int, changes: dict):
        session = Config.session
        project = session.query(Project).filter_by(projectid=projectid).one()

        modifieds = {}

        if not project:
            raise Exception("Project not found")

        for item in changes.items():
            if item[1] != '':
                modifieds[f"{item[0]}"] = item[1]

        if "title" in modifieds.keys():
            project.title = modifieds["title"]

        if "shortdescription" in modifieds.keys():
            project.shortdescription = modifieds["short"]

        if "bigdescription" in modifieds.keys():
            project.bigdescription = modifieds["big"]

        if "link" in modifieds.keys():
            project.link = modifieds["link"]

        if "media" in modifieds.keys():
            project.media = modifieds["media"]

        if "active" in modifieds.keys():
            project.active = bool(int(modifieds["active"]))

        session.commit()

    def get_projects(self, orderby: str = "recent"):
        session = Config.session
        projects = session.query(Project).filter(Project.active == True).all()
        if orderby:
            if orderby == "recent":
                projects = session.query(Project).filter(Project.active == True).order_by(Project.datecreated.desc()).all()

            if orderby == "old":
                projects = session.query(Project).filter(Project.active == True).order_by(Project.datecreated.asc()).all()

        return projects

    def get_project_by_id(self, projectid: int):
        session = Config.session
        project = session.query(Project).filter(Project.projectid==projectid).one()

        if not project:
            raise Exception("Project not found")

        return project

    def get_projects_to_home(self) -> list:
        session = Config.session
        all_projects = session.query(Project).filter(Project.active==True).all()
        projects = [project for project in all_projects]
        projects_to_home = []
        for i in range(4):
            project = choice(projects)
            projects_to_home.append(project)
            projects.remove(project)

        return projects_to_home




