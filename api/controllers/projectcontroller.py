from typing import List, Optional

from api.controllers import BaseController
from api.db.models.Project import Project
from api.db.query_utils.project import ProjectQueryUtils


class ProjectController(BaseController):
    def get_all_projects(self, page: int, perpage: int, status: bool, tags: List[str]) -> List[Project]:
        query = ProjectQueryUtils(self.session).get_all_objects_query(Project)

        if status:
            query = query.filter(Project.active == True)

        if tags:
            query = query.filter(Project.tags.icontains(tags))

        if page or perpage:
            query = ProjectQueryUtils(self.session).get_all_objects_paginated(Project, page, perpage)

        return query.all()

    def get_project_by_id(self, project_id: int) -> Optional[Project]:
        project = ProjectQueryUtils(self.session).get_object_by_id(Project, project_id)

        if not project:
            raise Exception(f"Project id: {project_id} not found.")

        return project
