"""This unit contains a MovieDao class to work with a movie table"""
from flask_sqlalchemy import SQLAlchemy
# ---------------------------------------------------------------------------


class MovieDao:
    """The MovieDao class provides all necessary logic to work with
    a movie table"""

    def __init__(self, db: SQLAlchemy, model, schema) -> None:
        """Initial method of the MovieDao class

        :param db: the SQLAlchemy instance
        :param model: the Movie class' model
        :param schema: an instance of the Schema class
        """
        self.db = db
        self.model = model
        self.schema = schema

    def get_all(self, page: int = 0) -> list:
        """This method returns a list of five movies

        :param page: the page number needed to calculate offset parameter

        :returns:
            movies_list - a list of dicts containing movies data
        """
        # calculating offset parameter
        if page in (0, 1):
            offset = 0

        elif page > 1:
            offset = (page - 1) * 5

        else:
            offset = 0

        session = self.db.session.query(self.model)
        all_movies = session.limit(5).offset(offset).all()

        movies_list = self.schema.dump(all_movies, many=True)

        return movies_list

    def get_by_id(self, movie_id: int) -> dict:
        """This method returns a dictionary containing data about a movie
        by provided id

        :param movie_id: the id of the searching movie

        :returns:
            movie_dict - a dictionary containing movie data
        """
        movie = self.model.query.filter(self.model.id == movie_id).one()

        movie_dict = self.schema.dump(movie)

        return movie_dict

    def get_by_director_id(self, director_id: int) -> list:
        """This method returns a list of movies found by director_id

        :param director_id: the id of the searching director

        :return:
            movies_list - a list of movies found by director_id
        """
        movies = self.model.query.filter(
            self.model.director_id == director_id).all()

        movies_list = self.schema.dump(movies, many=True)

        return movies_list

    def get_by_genre_id(self, genre_id: int) -> list:
        """This method returns a list of movies found by genre_id

        :param genre_id: the id of the searching genre

        :return:
            movies_list - a list of movies found by genre_id
        """
        movies = self.model.query.filter(self.model.genre_id == genre_id).all()

        movies_list = self.schema.dump(movies, many=True)

        return movies_list

    def get_by_genre_and_director(self, genre_id: int, director_id: int):
        """This method returns a list of movies found by both genre_id and
        director_id

        :param genre_id: the id of the searching genre
        :param director_id: the id of the searching director

        :returns:
            movies_list - a list of movies found by both genre_id
            and director_id
        """
        movies = self.model.query.filter(self.model.genre_id == genre_id,
                                         self.model.director_id == director_id
                                         ).all()

        movies_list = self.schema.dump(movies, many=True)

        return movies_list
