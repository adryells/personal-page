from typing import List

from api.controllers import BaseController
from api.db.models.Tag import Tag
from api.db.query_utils.tag import TagQueryUtils


class TagController(BaseController):
    def get_tag_by_id(self, tagid: int) -> Tag:
        tag = TagQueryUtils(self.session).get_object_by_id(Tag, tagid)

        if not tag:
            raise Exception(f"Tag id: {tagid} not found.")

        return tag

    def get_all_tags(self, page: int, perpage: int, active: bool) -> List[Tag]:
        query = TagQueryUtils(self.session).get_all_objects_query(Tag)

        if active is not None:
            query = query.filter(Tag.active == active)

        if page or perpage:
            query = TagQueryUtils(self.session).get_all_objects_paginated(Tag, page, perpage)

        return query.all()
