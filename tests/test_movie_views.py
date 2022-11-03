"""This file contains a TestMoviesViews class for testing purposes"""
import pytest
from tests.testing_configs import MOVIE_KEYS, ROUTES_GET_ALL, VALUES_GET_ONE
from app import app
# -----------------------------------------------------------------------


@pytest.fixture()
def test_app():
    """This is a fixture for returning a test client

    :returns:
        test_client - a test client of the Flask app
    """
    test_client = app.test_client()

    return test_client
# -----------------------------------------------------------------------


class TestMoviesViews:
    """The TestMoviesViews class serves to test 'get_all' and 'get_one'
     methods of MoviesView class"""

    @pytest.mark.parametrize('route, movie_amount', ROUTES_GET_ALL)
    def test_get_all(self, test_app, route, movie_amount):
        """The method tests get_all method by using different routes

        :param test_app: a fixture for testing
        :param route: a current route to test
        :param movie_amount: the amount of movie that have to be received
        """
        request = test_app.get(route)
        all_movies = request.json

        assert request.status_code == 200, 'Ответ сервера не ОК'
        assert len(all_movies) == movie_amount, 'Неверное кол-во ' \
                                                'фильмов в ответе'
        # checking types and keys of all received movies
        for movie in all_movies:

            assert type(movie) is dict, 'Тип вложенных данных неверный'
            assert set(movie) == MOVIE_KEYS, 'Ключи не совпадают'

    def test_get_one(self, test_app):
        """The method tests get_one method of MovieView class

        :param test_app: a fixture for testing
        """
        request = test_app.get('/movies/1')
        movie = request.json

        assert request.status_code == 200, 'Ответ сервера не ОК'

        assert type(movie) is dict, 'Тип данные не словарь'
        assert set(movie) == MOVIE_KEYS, 'Ключи не совпадают'
        # checking values of received dictionary by route /movies/1
        assert set(movie.values()) == set(VALUES_GET_ONE.values()), \
            'Значения не совпадают'
