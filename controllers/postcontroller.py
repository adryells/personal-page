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

        if not post:
            raise Exception("Post not found")

        if "title" in changes.keys():
            post.title = changes["title"]

        if "description" in changes.keys():
            post.description = changes["description"]

        if "content" in changes.keys():
            post.content = changes["content"]

        if "media" in changes.keys():
            post.media = changes["media"]

        if "active" in changes.keys():
            post.active = changes["active"]

        if "tags" in changes.keys():
            post.tags = changes["tags"]

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