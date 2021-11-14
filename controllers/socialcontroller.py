from models.basemodel import Config, Social


class SocialController:

    def add_social(self, name: str, media: str, link: str, active: bool) -> Social:
        session = Config.session

        new_social = Social(
            name=name,
            link=link,
            media=media,
            active=active
        )

        session.add(new_social)
        session.commit()

        return new_social

    def update_social(self, socialid: int, changes: dict):
        session = Config.session
        social = session.query(Social).filter_by(socialid=socialid).one()

        if not social:
            raise Exception("Social not found")

        if "name" in changes.keys():
            social.name = changes["name"]

        if "link" in changes.keys():
            social.link = changes["link"]

        if "media" in changes.keys():
            social.media = changes["media"]

        if "active" in changes.keys():
            social.active = changes["active"]

        session.commit()

    def get_social_medias(self):
        session = Config.session
        socials = session.query(Social).all()

        if not socials:
            raise Exception("Don't have any social")

        return socials.__dict__()

    def get_social_by_id(self, socialid: int):
        session = Config.session
        social = session.query(Social).filter(socialid=socialid).one()

        if not social:
            raise Exception("Social not found")

        return social.__dict__()

