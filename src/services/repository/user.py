from core.models import User, db


class UserRepository(object):
    def __init__(self):
        self.db = db

    def get_user_by_email(self, email: str) -> User:
        return self.db.session.query(User).filter_by(email=email).first()

    def get_user_by_uid(self, uid: int) -> User:
        return self.db.session.query(User).filter_by(uid=uid).first()

    def add_user(self, user: User) -> User:
        self.db.session.add(user)
        self.db.session.commit()
        return user
