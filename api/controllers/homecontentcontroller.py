from typing import List

from api.controllers import BaseController
from api.db.models.HomeContent import HomeContent
from api.db.query_utils.homecontent import HomeContentQueryUtils


class HomeContentController(BaseController):
    def get_all_home_contents(self, status: bool, page: int, perpage: int) -> List[HomeContent]:
        query = HomeContentQueryUtils(self.session).get_all_objects_query(HomeContent)

        if status:
            query = query.filter(HomeContent.active == status)

        if page or perpage:
            query = HomeContentQueryUtils(self.session).get_all_objects_paginated(HomeContent, page, perpage)

        return query.all()
