from models.basemodel import Comment, Config, Post


class CommentController:
    def add_comment(self, commenter:str = "Anonimo", content:str = None, postid:int = None, active:bool = True):
        session = Config.session

        post = session.query(Post).filter(Post.postid == postid).one()

        new_comment = Comment(
            commenter=commenter,
            content=content,
            active=active
        )

        post.comments.append(new_comment)

        session.add(new_comment)
        session.commit()

        return new_comment


    def update_comment(self, commentid: int, changes: dict):
        session = Config.session
        comment = session.query(Comment).filter(commentid=commentid).one()

        if not comment:
            raise Exception(f"Comment id: {commentid} not found")

        if changes["content"] in changes.keys():
            comment.content = changes["content"]

        if changes["active"] in changes.keys():
            comment.content = changes["active"]

        session.commit()

    def get_comments(self, active: bool):
        session = Config.session
        comments = session.query(Comment).filter(active=active).all()

        return comments

    def get_comment_by_id(self, commentid:int):
        session = Config.session

        if not commentid:
            raise Exception("You forgot the commentid")

        comment = session.query(Comment).filter(commentid=commentid).one()

        return comment

