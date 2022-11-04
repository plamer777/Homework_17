"""This file contains blueprint and CBV to work with '/genre/' routes"""
from flask import Blueprint, request
from flask_restx import Api, Resource
from app.movies_blueprint import movie_dao
from dao.genre_dao import GenreDao
from models.db_models import Genre
from sources.source import db, genre_schema
from utils import create_movies_by_genre_dict
# --------------------------------------------------------------------------

# creating all necessary objects
genre_blueprint = Blueprint('genre', __name__)
api = Api(genre_blueprint)
genre_ns = api.namespace('genres')
genre_dao = GenreDao(db, Genre, genre_schema)
# --------------------------------------------------------------------------


@genre_ns.route('/')
class GenresView(Resource):
    """The GenresView is a CBV to process routes like '/genres/'"""

    def get(self):
        """This method serves to process GET requests for routes like
        '/genres/'

        :returns:
            result - a tuple with a result of the GET request
        """
        result = genre_dao.get_all()

        return result

    def post(self):
        """This method serves to process POST requests for /genres/ route

        :returns:
            result - a tuple with a result of the POST request
        """
        new_genre = request.json

        result = genre_dao.add_new(new_genre)

        return result


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    """The GenreView is a CBV to process routes like
    '/genres/1'"""

    def get(self, genre_id):
        """This method serves to process GET requests for routes like
        '/genres/2'

        :param genre_id: the id of a searching genre

        :returns:
            result - a tuple with a result of the GET request
        """
        genre = genre_dao.get_by_id(genre_id)
        movies = movie_dao.get_by_genre_id(genre_id)
        result = create_movies_by_genre_dict(genre, movies)

        return result

    def put(self, genre_id: int):
        """This method serves to process PUT requests

        :param genre_id: the id of a record in the table

        :returns:
            result - a tuple with a result of the PUT request
        """
        new_data = request.json

        result = genre_dao.update(genre_id, new_data)

        return result

    def delete(self, genre_id):
        """This method serves to process DELETE requests

        :param genre_id: the id of a record in the table

        :returns:
            result - a tuple with a result of the DELETE request
        """
        result = genre_dao.delete(genre_id)

        return result
