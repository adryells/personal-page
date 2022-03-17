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

    def add_or_update_tag(self, portuguese_name: str = None, english_name: str = None, active: bool = True
        ) -> Tag:

        tag_db = TagQueryUtils(self.session).get_tag_by_name(portuguese_name)
        if tag_db:
            if english_name:
                tag_db.english_name = english_name
            if active is not None:
                tag_db.active = active

            self.session.commit()
            return tag_db

        tag = Tag(
            portuguese_name=portuguese_name,
            english_name=english_name,
            active=active
        )

        self.session.add(tag)
        self.session.commit()

        return tag
