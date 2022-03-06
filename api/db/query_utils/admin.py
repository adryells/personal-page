from api.db.models.Admin import Admin
from api.db.query_utils import DbBaseUtils


class AdminQueryUtils(DbBaseUtils):
    def get_admin_by_id(self, admin_id: int):
        admin = self.session.query(Admin).filter(Admin.id == admin_id).one_or_none()

        return admin