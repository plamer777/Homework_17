"""This unit serves to work with '/movies/' routes"""
from flask import Blueprint, request
from flask_restx import Resource, Api
from dao.movies_dao import MovieDao
from models.db_models import Movie
from utils import check_id_and_load_movies
from sources.source import db, movie_schema
# ------------------------------------------------------------------------

# creating all necessary instances
movie_blueprint = Blueprint('movies', __name__)
api = Api(movie_blueprint)
movie_ns = api.namespace('movies')
movie_dao = MovieDao(db, Movie, movie_schema)
# ------------------------------------------------------------------------


@movie_ns.route('/')
class MoviesView(Resource):
    """This is a Class Based View working with get and post requests"""

    def get(self):
        """This method serves to process a GET requests excepting ones
        having id the route like /movies/3

        :returns:
            all_movies - a list of dicts with movie's data or 404 status code
            instead if data is not found
        """

        genre_id = int(request.args.get('genre_id', 0))
        director_id = int(request.args.get('director_id', 0))
        page_id = int(request.args.get('page_id', 0))

        # received movies' list depends on ids received from args
        result = check_id_and_load_movies(movie_dao, genre_id,
                                          director_id, page_id)

        return result

    def post(self):
        """This method serves to process a POST requests

        :returns:
            a tuple with a result of the request
        """
        received_movie = request.json

        result = movie_dao.add_new(received_movie)

        return result


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    """This class is CBW working with GET, PUT, PATCH and DELETE requests for a
    single movie found by provided id"""

    def get(self, movie_id: int):
        """This method returns a single movie found by a movie_id

        :param movie_id: the movie id for searching

        :returns:
            single_movie - a dict with found movie data
        """
        result = movie_dao.get_by_id(movie_id)

        return result

    def put(self, movie_id: int):
        """This method serves to process PUT requests

        :param movie_id: the id of the updated movie

        :returns:
            a tuple with a result of the request
        """
        new_data = request.json

        result = movie_dao.update(movie_id, new_data)

        return result

    def delete(self, movie_id: int):
        """This method processes DELETE requests

        :param movie_id: the id of the deleted movie

        :returns:
            a tuple with a result of the request
        """
        result = movie_dao.delete(movie_id)

        return result
