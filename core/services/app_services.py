from abc import abstractmethod

from .user_services import UserService
from .game_service import GameService

""" This is an abstract class call by AppServiceImpl class in src/service/app_service.py
    If the service or its functionality is not implemented then it will raised error.
"""


class AppService(object):
    @abstractmethod
    def get_user_service(self) -> UserService:
        raise NotImplementedError

    def get_game_service(self) -> GameService:
        raise NotImplementedError
