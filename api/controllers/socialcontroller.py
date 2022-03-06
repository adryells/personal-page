from typing import List, Optional

from api.controllers import BaseController
from api.db.models.Social import Social
from api.db.query_utils.social import SocialQueryUtils


class SocialController(BaseController):
    def get_all_socials(self, page: int, perpage: int) -> List[Social]:
        socials = SocialQueryUtils(self.session).get_all_objects_query(Social)

        if page or perpage:
            socials = SocialQueryUtils(self.session).get_all_objects_paginated(Social, page, perpage)

        return socials.all()

    def get_social_by_id(self, social_id: int) -> Optional[Social]:
        social = SocialQueryUtils(self.session).get_object_by_id(Social, social_id)

        if not social:
            raise Exception(f"Social id: {social_id} not found.")

        return social