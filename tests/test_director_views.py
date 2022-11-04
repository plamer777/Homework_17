"""This is a unit with TestDirectorGenresViews class that serves to test
'/directors/' and '/genres/' routes
"""
import pytest
from tests.test_movie_views import app
from tests.testing_configs.directors_genres_tests_config import \
    ROUTES_AND_AMOUNTS, KEYS, GENRE_AND_DIRECTOR_GET, ADD_NEW_DATA, \
    UPDATE_DATA, DELETING
from utils import check_records_list, check_request
# ------------------------------------------------------------------------


@pytest.fixture()
def test_app():
    """The fixture for testing purposes

    :returns:
        test_client - a test application
    """
    test_client = app.test_client()

    return test_client
# ------------------------------------------------------------------------


class TestDirectorGenresViews:
    """The TestDirectorGenresViews class provides all methods to test
    '/directors/' and '/genres/' routes
    """
    @pytest.mark.parametrize('route, amount', ROUTES_AND_AMOUNTS)
    def test_get_all(self, test_app, route, amount):
        """This method tests GET requests to /directors/ and /genres/ routes

        :param test_app: the fixture for testing purposes
        :param route: a current testing route
        :param amount: an anticipated amount of records in received list
        """
        request = test_app.get(route)

        assert request.status_code == 200, 'Ответ сервера не ОК'

        records = request.json

        check_records_list(records, amount, KEYS)

    @pytest.mark.parametrize('route, record, keys', GENRE_AND_DIRECTOR_GET)
    def test_get_one(self, test_app, route, record, keys):
        """This method tests GET request on routes like /genres/1 and
        /directors/1

        :param test_app: the fixture for testing purposes
        :param route: a current testing route
        :param record: a dictionary containing data to compare with received
        data
        :param keys: a list of keys to compare with ones in received json
        """
        request = test_app.get(f'{route}1')

        check_request(request, keys, record)

    @pytest.mark.parametrize('route, record, keys', ADD_NEW_DATA)
    def test_add_new(self, test_app, route, record, keys):
        """This method tests POST request on routes like /genres/1 and
        /directors/1

        :param test_app: the fixture for testing purposes
        :param route: a current testing route
        :param record: a dictionary containing data to add in database
        :param keys: a list of keys to check added record
        """
        request = test_app.post(route, json=record)

        assert request.status_code == 201, 'Данные не добавлены'

        request = test_app.get(f'{route}{record["id"]}')

        # this action is needed because
        # the received json has an additional key added by the application
        if 'movies' in keys:
            record['movies'] = 'Not Found'

        check_request(request, keys, record)

    @pytest.mark.parametrize('route, record, keys', UPDATE_DATA)
    def test_update(self, test_app, route, record, keys):
        """This method tests PUT request on routes
        like /genres/1 and /directors/1

        :param test_app: the fixture for testing purposes
        :param route: a current testing route
        :param record: a dictionary containing data to update
        :param keys: a list of keys to check updated record
        """
        request = test_app.put(f'{route}{record["id"]}', json=record)

        assert request.status_code == 204, 'Данные не обновлены'

        request = test_app.get(f'{route}{record["id"]}')

        if 'movies' in keys:
            record['movies'] = 'Not Found'

        check_request(request, keys, record)

    @pytest.mark.parametrize('route, pk', DELETING)
    def test_delete(self, test_app, route, pk):
        """This method tests DELETE request

        :param test_app: the fixture for testing purposes
        :param route: a current testing route
        :param pk: an id of deleted record
        """
        request = test_app.delete(f'{route}{pk}')

        assert request.status_code == 204, 'Данные не удалены'

        request = test_app.get(f'{route}{pk}')

        assert request.status_code == 404, 'Запись все еще не удалена'
