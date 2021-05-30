from core.services.game_service import GameService
from core.models import Game, db
from core.exceptions.base_error import BaseError
from src.services.repository.game import GameRepository
from src.services.app_services import AppService

""" This files is an login implementation of Game functionality.
    In view the below function will get call through services module.
    It takes GameService as abstract class which is in core/service/game_service.py
"""


class GameServiceImpl(GameService):

    def __init__(self, game_repository: GameRepository, services: AppService, config):
        self.game_repository = game_repository
        self.services = services
        self.config = config

    def update_games(self, data: list):
        game_error = BaseError()
        gid_list = [str(i['gid']) for i in data]
        try:
            all_data_objs = self.game_repository.get_games_in_bulk(data=gid_list)

            for j in range(len(all_data_objs)):
                all_data_objs[j].title = data[j]['title']
                all_data_objs[j].platform = data[j]['platform']
                all_data_objs[j].score = data[j]['score']
                all_data_objs[j].genre = data[j]['genre']
                all_data_objs[j].editors_choice = data[j]['editors_choice']

            db.session.commit()
            game_error.global_error['data'] = gid_list
            game_error.global_error['message'] = "Updated the games"
        except Exception as e:
            print(e)
            game_error.has_error = True
            game_error.global_error['has_error'] = True
            game_error.global_error['message'] = "Something Went Wrong"
            game_error.global_error['data'] = gid_list = [str(i['gid']) for i in data]
            db.session.rollback()

        return game_error

    def add_games(self, game: [Game]):
        game_error = BaseError()

        game_add_details = self.game_repository.add_games(game=game)
        if len(game_add_details) == len(game):
            game_error.global_error['message'] = "Games Added Successfully"
        else:
            game_error.has_error = True
            game_error.global_error['has_error'] = True
            game_error.global_error['message'] = "Games Not added"
        return game_error

    def get_game_by_title(self, title: str):
        game_error = BaseError()

        fetched_game = self.game_repository.get_game_by_title(title=title)

        if fetched_game is None:
            game_error.has_error = True
            game_error.global_error['has_error'] = True
            game_error.global_error['data'] = title
            game_error.global_error['message'] = "Game not available"
        else:
            game_details = {"gid": fetched_game.gid, 'title': fetched_game.title, 'genre': fetched_game.genre,
                            'platform': fetched_game.platform, 'editors_choice': fetched_game.editors_choice,
                            'score': fetched_game.score}

            game_error.global_error['data'] = game_details
            game_error.global_error['message'] = "Game available"
        return game_error

    def get_games_by_filter(self, inputs: dict):
        game_error = BaseError()
        get_all_games = self.game_repository.get_all_games(filter_dict=inputs)

        if get_all_games is None:
            game_error.has_error = True
            game_error.global_error['has_error'] = True
            game_error.global_error['message'] = "No such games available"
        else:
            all_games = []
            for one_game in get_all_games:
                game = {"gid": one_game.gid, 'title': one_game.title, 'genre': one_game.genre,
                 'platform': one_game.platform, 'editors_choice': one_game.editors_choice,
                 'score': one_game.score}
                all_games.append(game)

            game_error.global_error['data'] = all_games
            game_error.global_error['message'] = "success"
        return game_error

    def delete_games_by_id(self, ids: int):
        game_error = BaseError()
        get_game = self.game_repository.get_game_by_id(ids=ids)
        if get_game is None:
            game_error.global_error['has_error'] = True
            game_error.global_error['Message'] = "Game not found"
            game_error.global_error['data'] = ids
            return game_error
        game_details = self.game_repository.delete_game_by_id(ids=ids)

        game_error.global_error['message'] = "Game deleted"
        game_error.global_error['data'] = ids
        return game_error





