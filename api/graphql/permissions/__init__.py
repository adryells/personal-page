import re
from functools import wraps

from fastapi import Depends
from sqlalchemy.orm import Session

from api.controllers import BaseController
from api.db import get_session

from api.db.query_utils.admin import AdminQueryUtils
from api.graphql.util import WaverGraphQLResolveInfo


class GraphqlAuth(BaseController):

    def __init__(self,
                 permission: str,
                 db_session: Session = Depends(get_session),
                 allow_anonymous=False):

        self.permission = permission
        self.allow_anonymous = allow_anonymous
        self.session = db_session

        super(GraphqlAuth, self).__init__(db_session)

    def __call__(self, fn):
        @wraps(fn)
        def check_graphql_auth_decorator(*args, **kwargs):

            graphql_info: WaverGraphQLResolveInfo = args.__getitem__(1)

            authorization = graphql_info.context.authorization

            if not authorization:
                raise Exception("You're not logged.")

            try:
                header_token = re.match("Bearer (.+)", authorization).group(1)
                admin = AdminQueryUtils(graphql_info.context.session)\
                    .get_admin_by_token(header_token)

                if not admin:
                    raise Exception("Invalid Token.")

            except AttributeError:
                raise Exception("Invalid Token.")

            graphql_info.context.admin = admin

            return fn(*args, **kwargs)

        return check_graphql_auth_decorator
