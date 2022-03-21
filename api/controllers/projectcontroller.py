from typing import List, Optional

from api.controllers import BaseController
from api.db.models.Project import Project
from api.db.models.Tag import Tag, tag_projects
from api.db.query_utils.project import ProjectQueryUtils
from api.db.query_utils.tag import TagQueryUtils


class ProjectController(BaseController):
    def get_all_projects(self, page: int, perpage: int, status: bool, tags: List[str]) -> List[Project]:
        query = ProjectQueryUtils(self.session).get_all_objects_query(Project)

        if status is not None:
            query = query.filter(Project.active == status)

        if tags:
            tag_ids = [TagQueryUtils(self.session).get_tag_by_name(tag).id for tag in tags]
            query = query.join(tag_projects, Tag).filter(Tag.id.in_(tag_ids))

        if page or perpage:
            query = ProjectQueryUtils(self.session).paginate_query(query, page, perpage)

        return query.all()

    def get_project_by_id(self, project_id: int) -> Optional[Project]:
        project = ProjectQueryUtils(self.session).get_object_by_id(Project, project_id)

        if not project:
            raise Exception(f"Project id: {project_id} not found.")

        return project

    def update_project(self, project_id: int, title: str, english_title: str,
                       description: str, english_decription: str, bigdescription: str, english_bigdescription: str,
                       link: str, media: str, active: bool, datecreated: str, tags: List[str]) -> Project:
        project = ProjectQueryUtils(self.session).get_object_by_id(Project, project_id)

        if not project:
            raise Exception(f"Project id: {project_id} not found.")

        # TODO: Criar um handle
        if title: project.title = title
        if english_title: project.english_title = english_title
        if description: project.description = description
        if english_decription: project.english_description = english_decription
        if bigdescription: project.bigdescription = bigdescription
        if english_bigdescription: project.english_bigdescription = english_bigdescription
        if link: project.link = link
        if media: project.media = media
        if active is not None: project.active = active
        if datecreated: project.datecreated = datecreated
        if tags: # TODO: Otimizar isso aq embaixo
            for tag in tags:
                if tag not in project.tags:
                    project.tags.append( ## TODO: Adicionar situação de adição de tag inexistente, criar automaticmente
                        TagQueryUtils(self.session).get_tag_by_name(tag)
                    )

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
            new_project.tags = [TagQueryUtils(self.session).get_tag_by_name(tag) for tag in tags]

        self.session.add(new_project)
        self.session.commit()

        return new_project

