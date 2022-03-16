from typing import Optional

from sqlalchemy import or_

from api.db.models.Tag import Tag
from api.db.query_utils import DbBaseUtils


class TagQueryUtils(DbBaseUtils):
    def get_tag_by_name(self, name: str) -> Optional[Tag]:
        tag = self.session.query(Tag).filter(or_(Tag.portuguese_name == name, Tag.english_name == name)).one_or_none()

        return tag
