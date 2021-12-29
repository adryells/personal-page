from models.basemodel import Admin, Config, HomeContent


class HomeContentController:
    session = Config.session

    def get_actual_who_i_am(self):
        whoiam = self.session.query(HomeContent).filter(HomeContent.theme == "whoiam").one()

        return whoiam

    def get_actual_what_i_do(self):
        whatido = self.session.query(HomeContent).filter(HomeContent.theme == "whatido").one()

        return whatido

    def change_actual_content_from_theme(self, theme: str = None, new_content: str = None):
        theme_content = self.session.query(HomeContent).filter(HomeContent.theme == theme).one()

        theme_content.content = new_content

        self.session.commit()

    def get_all_contents(self):
        contents = self.session.query(HomeContent).all()

        return contents


