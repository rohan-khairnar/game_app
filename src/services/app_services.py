from core.services.app_services import AppService
from core.services.user_services import UserService
from .repository.user import UserRepository
from .impl.user_impl import UserServiceImpl
from core.services.game_service import GameService
from .impl.game_service_impl import GameServiceImpl
from .repository.game import GameRepository

""" this class is used to serve the functionality, database operations.
    this class takes AppService abstract class.
"""


class AppServicesImpl(AppService):
    def get_user_service(self) -> UserService:
        return self.user_service

    def get_game_service(self) -> GameService:
        return self.game_service

    def __init__(self, config):
        self.config = config
        self.__init_user_service()
        self.__init_game_service()

    def __init_user_service(self):
        user_repository = UserRepository()
        self.user_service = UserServiceImpl(user_repository, self, self.config)

    def __init_game_service(self):
        game_repository = GameRepository()
        self.game_service = GameServiceImpl(game_repository, self, self.config)
