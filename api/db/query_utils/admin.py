from typing import Optional

from api.db.models.Admin import Admin
from api.db.query_utils import DbBaseUtils


class AdminQueryUtils(DbBaseUtils):

    def get_admin_by_token(self, header_token: str) -> Optional[Admin]:
        admin = self.session.query(Admin).filter(Admin.token == header_token).one_or_none()

        return admin