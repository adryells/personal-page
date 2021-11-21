from models.basemodel import Config, Post


class PostController:

    def add_post(self, title: str, description: str, content:str, published:bool, media:str, active:bool) -> Post:
        session = Config.session

        new_post = Post(
            title=title,
            description=description,
            content=content,
            published=published,
            media=media,
            active=active
            )

        session.add(new_post)
        session.commit()

        return new_post

    def update_post(self, postid: int, changes: dict):
        session = Config.session
        post = session.query(Post).filter_by(postid=postid).one()

        if not post:
            raise Exception("Post not found")

        if "title" in changes.keys():
            post.title = changes["title"]

        if "description" in changes.keys():
            post.description = changes["description"]

        if "content" in changes.keys():
            post.content = changes["content"]

        if "published" in changes.keys():
            post.published = changes["published"]

        if "media" in changes.keys():
            post.media = changes["media"]

        if "active" in changes.keys():
            post.active = changes["active"]

        session.commit()

    def get_posts(self):
        session = Config.session
        posts = session.query(Post).filter(Post.active == True).all()

        return posts

    def get_post_by_id(self, postid: int):
        session = Config.session
        post = session.query(Post).filter(Post.postid==postid).one()

        if not post:
            raise Exception("Post not found")

        return post
