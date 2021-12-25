from models.basemodel import Config, Post, Tag
from bs4 import BeautifulSoup
import requests
import asyncio


class PostController:

    def add_post(self, title: str, description: str, content:str, media:str, active:bool, tags: list) -> Post:
        session = Config.session

        new_post = Post(
            title=title,
            description=description,
            content=content,
            media=media,
            active=active,
            )

        tags = [session.query(Tag).filter(Tag.tagid == tagid).one() for tagid in tags]
        for tag in tags:
            new_post.tags.append(tag)

        session.add(new_post)
        session.commit()

        return new_post

    def update_post(self, postid: int, changes: dict):
        session = Config.session
        post = session.query(Post).filter_by(postid=postid).one()
        modifieds = {}

        if not post:
            raise Exception("Post not found")

        for item in changes.items():
            if item[1] != '':
                # modifieds.append({f"{item[0]}": f"{item[1]}"})
                modifieds[f"{item[0]}"] = item[1]

        if "title" in modifieds:
            post.title = modifieds["title"]

        if "description" in modifieds:
            post.description = modifieds["description"]

        if "content" in modifieds:
            post.content = modifieds["content"]

        if "media" in modifieds:
            post.media = modifieds["media"]

        if "active" in modifieds:
            post.active = bool(modifieds["active"])

        if "tags" in modifieds:
            post.tags = modifieds["tags"]

        session.commit()

    def get_posts(self, orderby: str = "recent"):
        session = Config.session

        posts = session.query(Post).filter(Post.active == True).order_by(Post.datecreated.desc()).all()
        if orderby:
            if orderby == "recent":
                posts = session.query(Post).filter(Post.active == True).order_by(Post.datecreated.desc()).all()

            if orderby == "old":
                posts = session.query(Post).filter(Post.active == True).order_by(Post.datecreated.asc()).all()

        return posts

    def get_post_by_id(self, postid: int) -> Post:
        session = Config.session
        post = session.query(Post).filter(Post.postid==postid).one_or_none()

        if not post:
            return False

        return post