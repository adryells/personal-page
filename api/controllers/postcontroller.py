from typing import List, Optional

from api.controllers import BaseController
from api.db.models.Post import Post
from api.db.models.Tag import Tag, tag_posts
from api.db.query_utils.post import PostQueryUtils
from api.db.query_utils.tag import TagQueryUtils


class PostController(BaseController):
    def get_all_posts(self, page: int, perpage: int, status: bool, tags: List[str]) -> List[Post]:
        query = PostQueryUtils(self.session).get_all_objects_query(Post)

        if tags:
            tag_ids = [TagQueryUtils(self.session).get_tag_by_name(tag).id for tag in tags]
            query = query.join(tag_posts, Tag).filter(Tag.id.in_(tag_ids))

        if status is not None:

            query = query.filter(Post.active == status)

        if page or perpage:
            query = PostQueryUtils(self.session).get_all_objects_paginated(Post, page, perpage)

        return query.all()

    def get_post_by_id(self, post_id: int) -> Optional[Post]:
        post = PostQueryUtils(self.session).get_object_by_id(Post, post_id)

        if not post:
            raise Exception(f"Post id: {post_id} not found.")

        return post


