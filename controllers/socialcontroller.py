from models.basemodel import Config, Social


class SocialController:

    def add_social(self, name: str, media: str, link: str, active: bool) -> Social:
        session = Config.session

        new_social = Social(
            name=name,
            link=link,
            media=media,
            active=bool(active)
        )

        session.add(new_social)
        session.commit()

        return new_social

    def update_social(self, socialid: int, changes: dict):
        session = Config.session
        social = session.query(Social).filter_by(socialid=socialid).one()
        modifieds = {}

        if not social:
            raise Exception("Social not found")

        for item in changes.items():
            if item[1] != '':
                modifieds[f"{item[0]}"] = item[1]

        if "name" in modifieds.keys():
            social.name = modifieds["name"]

        if "link" in modifieds.keys():
            social.link = modifieds["link"]

        if "media" in modifieds.keys():
            social.media = modifieds["media"]

        if "active" in modifieds.keys():
            active = bool(int(modifieds["active"]))
            social.active = active

        session.commit()

    def get_social_medias(self):
        session = Config.session
        socials = session.query(Social).filter(Social.active == True).all()

        return socials

