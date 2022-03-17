from typing import List

from api.controllers import BaseController
from api.db.models.Post import Post
from api.db.models.Project import Project
from api.db.models.Tag import Tag
from api.db.query_utils.post import PostQueryUtils
from api.db.query_utils.project import ProjectQueryUtils
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

    def remove_tag_from(self, post_id: int = None, project_id: int = None, tag_id: int = None) -> bool:
        if post_id:
            post = PostQueryUtils(self.session).get_object_by_id(Post, post_id)

            if not post:
                raise Exception(f"Post id: {post_id} not found.")

            tag = self.check_if_tag_exists(tag_id)

            post.tags.remove(tag[1])

            self.session.commit()

            return True

        if project_id:

            project = ProjectQueryUtils(self.session).get_object_by_id(Project, post_id)

            if not project:
                raise Exception(f"Post id: {project_id} not found.")

            tag = self.check_if_tag_exists(tag_id)

            project.tags.remove(tag[1])

            self.session.commit()

            return True

        return False

    def check_if_tag_exists(self, tag_id: int) -> (bool, Tag):

        tag = TagQueryUtils(self.session).get_object_by_id(Tag, tag_id)

        if not tag:
            raise Exception(f"Tag id: {tag_id} not found.")

        return True, tag
