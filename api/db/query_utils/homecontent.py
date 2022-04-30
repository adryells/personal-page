from typing import List, Optional

from api.db.models.HomeContent import HomeContentType
from api.db.query_utils import DbBaseUtils


class HomeContentQueryUtils(DbBaseUtils):
    def get_all_home_content_types(self) -> List[HomeContentType]:
        home_content_types = self.session.query(HomeContentType).all()

        return home_content_types

    def get_home_content_type_by_slug(self, slug: str) -> Optional[HomeContentType]:
        home_content_type = self.session.query(HomeContentType).filter(HomeContentType.slug == slug).one_or_none()

        return home_content_type

