from models.basemodel import Admin, Config


class AdminController:

    def validate_admin_exists(self, username: str, password: str):
        session = Config.session

        admin = session.query(Admin).filter(Admin.username == username).one_or_none()
        if not admin:
            raise Exception("Admin not found")

        self.check_password(self, password=password, admin=admin)

        admin.status = True

        return admin.status
    def check_password(self, password: str, admin: Admin):
        if admin.password != password:
            raise Exception("Password is incorrect")

        return True

