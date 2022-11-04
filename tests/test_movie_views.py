"""This file contains a TestMoviesViews class for testing purposes"""
import pytest
from tests.testing_configs.movies_cbv_config import MOVIE_KEYS, \
    ROUTES_GET_ALL, VALUES_GET_ONE, NEW_MOVIE, UPDATED_MOVIE
from run import app
from utils import check_request, check_records_list
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

        assert request.status_code == 200, 'Ответ сервера не ОК'

        all_movies = request.json
        check_records_list(all_movies, movie_amount, MOVIE_KEYS)

    def test_get_one(self, test_app):
        """The method tests get_one method of MovieView class

        :param test_app: a fixture for testing
        """
        request = test_app.get('/movies/1')
        check_request(request, MOVIE_KEYS, VALUES_GET_ONE)

    def test_add_new(self, test_app):
        """The method tests POST request by '/movies/' route

        :param test_app: a fixture for testing
        """
        request = test_app.post('/movies/', json=NEW_MOVIE)

        assert request.status_code == 201, 'Данные не добавлены'

        request = test_app.get('/movies/25')
        check_request(request, MOVIE_KEYS, NEW_MOVIE)

    def test_update(self, test_app):
        """The method serves to test PUT request by '/movies/25' route

        :param test_app: a fixture for testing
        """
        request = test_app.put('/movies/25', json=UPDATED_MOVIE)

        assert request.status_code == 204, 'Данные не обновлены'

        request = test_app.get('/movies/25')
        check_request(request, MOVIE_KEYS, UPDATED_MOVIE)

    def test_delete(self, test_app):
        """The method serves to test DELETE request by '/movies/25' route

        :param test_app: a fixture for testing
        """
        request = test_app.delete('/movies/25')

        assert request.status_code == 204, 'Данные не были удалены'

        request = test_app.get('/movies/25')

        assert request.status_code == 404, 'Запись по прежнему в базе данных'
