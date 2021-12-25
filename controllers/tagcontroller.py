
from random import choice

from sqlalchemy import select

from models.basemodel import Config, tag_posts, tag_projects, Tag, Post, Project
from sqlalchemy.inspection import inspect


class TagController:

    def add_tag(self, name: str) -> Tag:
        session = Config.session

        tag = Tag(name=name)

        session.add(tag)
        session.commit()


    def update_tag(self, tagid: int, name: str):
        session = Config.session
        tag = session.query(Tag).filter_by(tagid=tagid).one()

        if not tag:
            raise Exception("Tag not found")

        tag.name = name

        session.commit()

    def get_tags(self) -> list:
        session = Config.session

        projects = session.query(Tag).filter(Tag.active == True).all()

        return projects

    def get_tag_by_id(self, tagid: int) -> Tag:
        session = Config.session
        tag = session.query(Tag).filter(Tag.tagid==tagid).one()

        if not tag:
            raise Exception("Tag not found")

        return tag

    def get_tag_by_name(self, name: str) -> Tag:
        session = Config.session
        tag = session.query(Tag).filter(Tag.name == name).one()

        if not tag:
            raise Exception("Tag not found")

        return tag

    def get_tags_from_post(self, postid: int) -> list:
        session = Config.session

        object = session.query(tag_posts).filter(tag_posts.constraints == postid).all()

        return object

    def get_tags_from_project(self, projectid: int) -> list:
        session = Config.session

        object = session.query(tag_projects).join(Project).filter(tag_projects.c.project_id == projectid).all()

        return object








