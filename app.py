"""This is a main file of the Flask application. There are six CBVs here"""
from flask_restx import Resource
from flask import request
from dao.movies_dao import MovieDao
from dao.director_dao import DirectorDao
from dao.genre_dao import GenreDao
from models.db_models import Movie, Director, Genre
from sources.source import movie_ns, db, app, movie_schema, director_schema, \
    director_ns, genre_ns, genre_schema
from utils import check_id_and_load_movies
# ----------------------------------------------------------------------

# creation of DAOs instances to work with a database
movie_dao = MovieDao(db, Movie, movie_schema)
director_dao = DirectorDao(db, Director, director_schema)
genre_dao = GenreDao(db, Genre, genre_schema)

# -------------------------------------------------------------------------


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
        try:
            genre_id = int(request.args.get('genre_id', 0))
            director_id = int(request.args.get('director_id', 0))
            page_id = int(request.args.get('page_id', 0))

        except Exception as e:

            print(f'Ошибка при получении данных из args - {e}')
            return 'Not Found', 404

        # received movies' list depends on ids received from args
        all_movies = check_id_and_load_movies(movie_dao, genre_id,
                                              director_id, page_id)

        if not all_movies:

            return 'Not Found', 404

        return all_movies, 200


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
        single_movie = movie_dao.get_by_id(movie_id)

        if not single_movie:

            return 'Not Found', 404

        return single_movie, 200
# -------------------------------------------------------------------------


@director_ns.route('/')
class DirectorsView(Resource):
    """The DirectorsView is a CBV to process routes like '/directors/'"""

    def post(self):
        """This method serves to process POST requests

        :returns:
            result - a tuple with a result of the POST request
        """
        new_director = request.json

        result = director_dao.add_new(new_director)

        return result


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    """The DirectorView is a CBV to process routes like
    '/directors/1'"""

    def put(self, director_id: int):
        """This method serves to process PUT requests

        :param director_id: an id of a record in the table

        :returns:
            result - a tuple with a result of the PUT request
        """
        new_data = request.json

        result = director_dao.update(director_id, new_data)

        return result

    def delete(self, director_id):
        """This method serves to process DELETE requests

        :param director_id: the id of a record in the table

        :returns:
            result - a tuple with a result of the DELETE request
        """
        result = director_dao.delete(director_id)

        return result
# -------------------------------------------------------------------------


@genre_ns.route('/')
class GenresView(Resource):
    """The GenresView is a CBV to process routes like '/genres/'"""

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
# -------------------------------------------------------------------------


@app.errorhandler(404)
def error_404(error_code):
    """This error handler processes 404 errors

    :param error_code: an error code caught up by the handler
    """
    return f'К сожалению страница не найдена, код ошибки - {error_code}'
# --------------------------------------------------------------------------


if __name__ == '__main__':
    app.run()
