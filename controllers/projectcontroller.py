from models.basemodel import Config, Project
from sqlalchemy import select

class ProjectController:

    def add_project(self, title: str, shortdescription: str, bigdescription: str, published: bool, media: str, link: str, active: bool) -> Project:
        session = Config.session

        new_project = Project(
            title=title,
            shortdescription=shortdescription,
            bigdescription=bigdescription,
            link=link,
            published=published,
            media=media,
            active=active
        )

        session.add(new_project)
        session.commit()

        return new_project

    def update_project(self, projectid: int, changes: dict):
        session = Config.session
        project = session.query(Project).filter_by(projectid=projectid).one()

        if not project:
            raise Exception("Project not found")

        if "title" in changes.keys():
            project.title = changes["title"]

        if "shortdescription" in changes.keys():
            project.shortdescription = changes["shortdescription"]

        if "bigdescription" in changes.keys():
            project.bigdescription = changes["bigdescription"]

        if "link" in changes.keys():
            project.link = changes["link"]

        if "published" in changes.keys():
            project.published = changes["published"]

        if "media" in changes.keys():
            project.media = changes["media"]

        if "active" in changes.keys():
            project.active = changes["active"]

        session.commit()

    def get_projects(self) -> list:
        session = Config.session

        projects = session.query(Project).filter(Project.active == True).all()


        return projects

    def get_project_by_id(self, projectid: int):
        session = Config.session
        project = session.query(Project).filter(Project.projectid==projectid).one()

        if not project:
            raise Exception("Project not found")

        return project

