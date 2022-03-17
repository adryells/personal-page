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

    def add_home_content(self,
                         content: str,
                         homecontenttype: str,
                         active: bool,
                         datecreated: str
                         ):
        new_home_content = HomeContent(
            content=content,
            homecontenttype=homecontenttype,
            active=active,
            datecreated=datecreated
        )

        self.session.add(new_home_content)
        self.session.commit()

        return new_home_content

    def update_home_content(self,
                         home_content_id: int,
                         content: str,
                         homecontenttype: str,
                         active: bool,
                         datecreated: str
                         ):
        home_content = HomeContentQueryUtils(self.session).get_object_by_id(HomeContent, home_content_id)
        if not home_content:
            raise Exception("Home Content not found.")

        if content: home_content.content = content
        if homecontenttype: home_content.homecontenttype = homecontenttype
        if active is not None: home_content.active = active
        if datecreated: home_content.datecreated = datecreated

        self.session.commit()

        return home_content

