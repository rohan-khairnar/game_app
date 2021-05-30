from core.models import Game, db


class GameRepository(object):
    def __init__(self):
        self.db = db

    def get_game_by_title(self, title: str) -> Game:
        return self.db.session.query(Game).filter_by(title=title).first()

    def get_all_games(self, filter_dict: dict) -> [Game]:
        sort_type = Game.score.asc() if filter_dict['order_by'] == 'asc' else Game.score.desc()
        query = self.db.session.query(Game)
        if 'platform' in filter_dict.keys():
            query = query.filter_by(platform=filter_dict['platform'])
        if 'genre' in filter_dict.keys():
            query = query.filter_by(genre=filter_dict['genre'])
        if 'editors_choice' in filter_dict.keys():
            query = query.filter_by(editors_choice=filter_dict['editors_choice'])
        return query.order_by(sort_type).all()

    def add_games(self, game: [Game]) -> Game:
        self.db.session.bulk_save_objects(game)
        self.db.session.commit()
        return game

    def delete_game_by_id(self, ids: list):
        self.db.session.query(Game).filter_by(gid=ids).delete()
        self.db.session.commit()

    def get_game_by_id(self, ids: int):
        return self.db.session.query(Game).filter_by(gid=ids).first()

    def get_games_in_bulk(self, data: list):
        all_obj = self.db.session.query(Game).filter(Game.gid.in_(data)).all()
        return all_obj
