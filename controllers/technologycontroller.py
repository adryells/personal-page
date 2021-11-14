from models.basemodel import Config, Technology


class TechnologyController:

    def add_tech(self, name: str, description: str, link:str, experience:str, media:str, situation:str, active: bool) -> Technology:
        session = Config.session

        new_tech = Technology(
            name=name,
            description=description,
            link=link,
            experience=experience,
            media=media,
            situation=situation,
            active=active
            )

        session.add(new_tech)
        session.commit()

        return new_tech

    def update_tech(self, techid: int, changes: dict):
        session = Config.session
        tech = session.query(Technology).filter_by(technologyid=techid).one()

        if not tech:
            raise Exception("Tech not found")

        if "name" in changes.keys():
            tech.name = changes["name"]

        if "description" in changes.keys():
            tech.description = changes["description"]

        if "link" in changes.keys():
            tech.link = changes["link"]

        if "experience" in changes.keys():
            tech.experience = changes["experience"]

        if "media" in changes.keys():
            tech.media = changes["media"]

        if "situation" in changes.keys():
            tech.situation = changes["situation"]

        if "active" in changes.keys():
            tech.active = changes["active"]

        session.commit()

    def get_technologies(self):
        session = Config.session
        technologies = session.query(Technology).all()

        if not technologies:
            raise Exception("Don't have any technologie")

        return technologies.__dict__()

    def get_technology_by_id(self, technologyid: int):
        session = Config.session
        technology = session.query(Technology).filter(technologyid=technologyid).one()

        if not technology:
            raise Exception("Technology not found")

        return technology.__dict__()
