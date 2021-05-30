from src import app, services
from core.models import Game
from core.exceptions.base_error import BaseError
from flask_login import login_required
from flask import request


@app.route(app.config['UPDATE_GAMES'], methods=["PUT"])
@login_required
def update_games():
    data = request.get_json()
    service = services.get_game_service()
    error_obj = service.update_games(data=data)
    return error_obj.global_error


@app.route(app.config['ADD_GAMES'], methods=["POST"])
@login_required
def add_games():
    try:
        data = request.get_json()
        games_objs = []
        for one_game in data:
            game_obj = Game()
            game_obj.title = one_game['title']
            game_obj.genre = one_game['genre']
            game_obj.score = one_game['score']
            game_obj.editors_choice = one_game['editors_choice']
            game_obj.platform = one_game['platform']
            games_objs.append(game_obj)

        service = services.get_game_service()
        error_obj = service.add_games(game=games_objs)

    except Exception as e:
        print(e)
        error_obj = BaseError()
        error_obj.global_error['has_error'] = True
        error_obj.global_error['message'] = "Something Went Wrong"
    return error_obj.global_error


@app.route(app.config['GET_GAME'])
@login_required
def get_game_title():
    try:
        game_service = services.get_game_service()
        title = request.args.get('title')
        error_obj = game_service.get_game_by_title(title=title)
    except Exception as e:
        error_obj = BaseError()
        error_obj.global_error['has_error'] = True
        error_obj.global_error['message'] = "Something Went Wrong"

    return error_obj.global_error

@app.route(app.config['GET_GAMES_FILTER'], methods=["POST"])
@login_required
def get_games_filter():
    try:
        game_service = services.get_game_service()
        filter_options = request.get_json()
        error_obj = game_service.get_games_by_filter(inputs=filter_options)

    except Exception as e:
        print(e)
        error_obj = BaseError()
        error_obj.global_error['has_error'] = True
        error_obj.global_error['message'] = "Something Went Wrong"

    return error_obj.global_error

@app.route(app.config['DELETE_GAMES'], methods=['DELETE'])
@login_required
def delete_games():
    error_obj = BaseError()
    try:
        data = request.get_json()
        ids = data['ids']
        game_service = services.get_game_service()
        error_obj = game_service.delete_games_by_id(ids=ids)
    except Exception as e:
        print(e)
        error_obj.global_error['has_error'] = True
        error_obj.global_error['message'] = "Something Went Wrong"
        error_obj.global_error['data'] = ids

    return error_obj.global_error
