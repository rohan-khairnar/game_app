from abc import abstractmethod

from core.models import Game


class GameService(object):
    @abstractmethod
    def add_games(self, game: Game):
        raise NotImplementedError

    def get_games(self, game: Game):
        raise NotImplementedError

    def update_games(self, data: list):
        raise NotImplementedError

    def delete_games_by_id(self, ids: int):
        raise NotImplementedError
