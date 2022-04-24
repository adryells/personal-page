from typing import List, Optional, Union

from api.controllers import BaseController
from api.controllers.tagcontroller import TagController
from api.db.models.Project import Project
from api.db.models.Tag import Tag, tag_projects
from api.db.query_utils.project import ProjectQueryUtils
from api.db.query_utils.tag import TagQueryUtils


class ProjectController(BaseController):
    def get_all_projects(self, page: int, perpage: int, status: bool, tags: List[str], order: str) -> List[Project]:
        query = ProjectQueryUtils(self.session).get_all_objects_query(Project)

        if status is not None:
            query = query.filter(Project.active == status)

        if tags:
            tag_ids = [TagQueryUtils(self.session).get_tag_by_name(tag).id for tag in tags]
            query = query.join(tag_projects, Tag).filter(Tag.id.in_(tag_ids))

        if order:
            order_options = {
                "RECENT": Project.datecreated.desc,
                "OLD": Project.datecreated.asc,
                "ALPHABETICAL": Project.title.asc,
                "REVERSE_ALPHA": Project.title.desc,
            }

            query = query.order_by(order_options[order.value]())

        if page or perpage:
            query = ProjectQueryUtils(self.session).paginate_query(query, page, perpage)

        return query.all()

    def get_project_by_id(self, project_id: int) -> Optional[Project]:
        project = ProjectQueryUtils(self.session).get_object_by_id(Project, project_id)

        if not project:
            raise Exception(f"Project id: {project_id} not found.")

        return project

    def update_simple_attribute(self, project: Project, attribute: str, new_value: Union[str, int]):
        if new_value != getattr(project, attribute):
            setattr(project, attribute, new_value)

    def update_project_tags(self, project: Project, tags: List[Tag]):
        for tag in tags:
            tag = TagController(self.session).add_or_update_tag(tag)

            if tag not in project.tags:
                project.tags.append(tag)

    def update_project(self, project_id: int, title: str, english_title: str,
                       description: str, english_decription: str, bigdescription: str, english_bigdescription: str,
                       link: str, media: str, active: bool, datecreated: str, tags: List[str]) -> Optional[Project]:

        project = ProjectQueryUtils(self.session).get_object_by_id(Project, project_id)

        if not project:
            raise Exception(f"Project id: {project_id} not found.")

        handler_attributes = {
            'title': lambda: self.update_simple_attribute(project, "title", title),
            'english_title': lambda: self.update_simple_attribute(project, "english_title", english_title),
            'description': lambda: self.update_simple_attribute(project, "description", description),
            'english_description': lambda: self.update_simple_attribute(project, "english_description",
                                                                       english_decription),
            'bigdescription': lambda: self.update_simple_attribute(project, "bigdescription", bigdescription),
            'english_bigdescription': lambda: self.update_simple_attribute(project, "english_bigdescription",
                                                                           english_bigdescription),
            'link': lambda: self.update_simple_attribute(project, "link", link),
            'media': lambda: self.update_simple_attribute(project, "media", media),
            'active': lambda: self.update_simple_attribute(project, "active", active),
            'datecreated': lambda: self.update_simple_attribute(project, "datecreated", datecreated),
            'tags': lambda: self.update_project_tags(project, tags)
        }

        for attribute, value in handler_attributes.items():
            handler_attributes[attribute]()

        self.session.commit()

        return project

    def add_project(
            self,
            title: str,
            english_title: str,
            description: str,
            bigdescription: str,
            english_description: str,
            english_bigdescription: str,
            media: str,
            link: str,
            tags: List[str],
            datecreated: str,
            active: bool
    ) -> Project:
        new_project = Project(
            title=title,
            english_title=english_title,
            description=description,
            english_description=english_description,
            bigdescription=bigdescription,
            media=media,
            link=link,
            datecreated=datecreated,
            active=active,
            english_bigdescription=english_bigdescription
        )

        if tags:
            [new_project.tags.append(TagController(self.session).add_or_update_tag(tag)) for tag in tags]

        self.session.add(new_project)
        self.session.commit()

        return new_project
