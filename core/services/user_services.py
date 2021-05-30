from abc import abstractmethod

from core.models import User


class UserService(object):
    @abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    def user_login(self, user: User):
        raise NotImplementedError
