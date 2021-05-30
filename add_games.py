import csv
from core.models import Game
from src.services.repository.game import GameRepository


def add_initial_games():
    # This function will use to add games data from csv file.
    # This function is called in src/__init__.py
    filename = "games_data.csv"
    games = []
    done = []
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            if str(line['title']) not in done:

                game_obj = Game()
                game_obj.title = str(line['title'])
                game_obj.genre = str(line['genre'])
                game_obj.score = float(line['score'])
                game_obj.platform = str(line['platform'])
                game_obj.editors_choice = str(line['editors_choice'])
                games.append(game_obj)
                done.append(str(line['title']))

        repo = GameRepository()
        repo.add_games(game=games)


