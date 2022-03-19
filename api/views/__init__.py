from .home_content_view import homecontent_router
from .tag_view import tag_router
from .data_view import data_router
from .post_view import blog_router
from .social_view import social_router
from .project_view import projects_router

views = [
    tag_router, data_router, blog_router, social_router, projects_router, homecontent_router
]