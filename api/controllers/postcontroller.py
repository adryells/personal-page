from typing import List, Optional

from api.controllers import BaseController
from api.controllers.tagcontroller import TagController
from api.db.models.Post import Post
from api.db.models.Project import Project
from api.db.models.Tag import Tag, tag_posts
from api.db.query_utils.post import PostQueryUtils
from api.db.query_utils.tag import TagQueryUtils


class PostController(BaseController):
    def get_all_posts(self, page: int, perpage: int, status: bool, tags: List[str], order: str) -> List[Post]:
        query = PostQueryUtils(self.session).get_all_objects_query(Post)

        if tags:
            tag_ids = [TagQueryUtils(self.session).get_tag_by_name(tag).id for tag in tags]
            query = query.join(tag_posts, Tag).filter(Tag.id.in_(tag_ids))

        if status is not None:
            query = query.filter(Post.active == status)

        if order:
            order_options = {
                "RECENT": Post.datecreated.desc,
                "OLD": Post.datecreated.asc,
                "ALPHABETICAL": Post.title.asc,
                "REVERSE_ALPHA": Post.title.desc,
            }

            query = query.order_by(order_options[order]())

        if page or perpage:
            query = PostQueryUtils(self.session).paginate_query(query, page, perpage)

        return query.all()

    def get_post_by_id(self, post_id: int) -> Optional[Post]:
        post = PostQueryUtils(self.session).get_object_by_id(Post, post_id)

        if not post:
            raise Exception(f"Post id: {post_id} not found.")

        return post

    def add_post(self,
                 title: str,
                 english_title: str,
                 description: str,
                 english_description: str,
                 content: str,
                 english_content: str,
                 media: str,
                 active: bool,
                 datecreated: str,
                 tags: List[str]
                 ) -> Post:

        post = Post(
            title=title,
            english_title=english_title,
            description=description,
            english_description=english_description,
            content=content,
            english_content=english_content,
            media=media,
            active=active,
            datecreated=datecreated
        )
        if tags:
            [post.tags.append(TagController(self.session).add_or_update_tag(tag)) for tag in tags]

        self.session.add(post)
        self.session.commit()

        return post

    def update_post(self,
                    post_id: int,
                    title: str,
                    english_title: str,
                    description: str,
                    english_description: str,
                    content: str,
                    english_content: str,
                    media: str,
                    active: bool,
                    datecreated: str,
                    tags: List[str]
                    ) -> Post:
        post = PostQueryUtils(self.session).get_object_by_id(Post, post_id)
        if not post:
            raise Exception(f"Post id: {post_id} not found.")

        if title: post.title = title
        if english_title: post.english_title = english_title
        if description: post.description = description
        if english_description: post.english_description = english_description
        if content: post.content = content
        if english_content: post.english_content = english_content
        if media: post.media = media
        if active is not None: post.active = active
        if datecreated: post.datecreated = datecreated
        if tags:
            for tag in tags:
                tag = TagController(self.session).add_or_update_tag(tag)
                post.tags.append(tag)

        self.session.commit()

        return post
