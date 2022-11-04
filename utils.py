"""There are serving functions in the unit"""


def check_id_and_load_movies(movie_dao, genre_id: int, director_id: int,
                             page_id: int) -> list:
    """This function checks provided ids and loads data from a table

    :param movie_dao: an instance of MovieDao class
    :param genre_id: the id of searching genre
    :param director_id: the id of searching director
    :param page_id: the id of desirable page (works only if previous ids wasn't
    provided)
    """
    # loading movies by provided both a genre_id and director_id
    if genre_id and director_id:
        all_movies = movie_dao.get_by_genre_and_director(
            genre_id, director_id)

    # loading movies if only genre_id was provided
    elif genre_id:
        all_movies = movie_dao.get_by_genre_id(genre_id)

    # loading movies if only director_id was provided
    elif director_id:
        all_movies = movie_dao.get_by_director_id(director_id)

    # loading all movies if either nothing or page_id was provided
    else:
        all_movies = movie_dao.get_all(page_id)

    return all_movies


def create_movies_by_genre_dict(genre: tuple, movies: tuple) -> tuple:
    """This function serves to add movies list to the genre dict

    :param genre: the dictionary containing genre data
    :param movies: the list of dictionaries with movies data

    :returns:
        genre - a tuple with updated dictionary and status code
    """
    if genre[1] == 200:

        genre[0]['movies'] = movies[0]

        return genre

    return 'Not Found', 404


def check_request(request, test_keys: set, test_dict: dict) -> None:
    """This function checks the request and compare received data with test
    data

    :param request: the TestRequest object
    :param test_keys: a set of test keys to check received json
    :param test_dict: a dictionary containing test data
    """
    assert request.status_code == 200, 'Ответ сервера не ОК'

    record = request.json

    assert type(record) is dict, 'Тип данные не словарь'
    assert set(record) == test_keys, 'Ключи не совпадают'

    # checking values of received dictionary
    assert set(record.values()) == set(test_dict.values()), \
        'Значения не совпадают'


def check_records_list(data_list: list, amount: int, test_keys: set):
    """This function is used to test a list of records

    :param data_list: a list of records to test
    :param amount: a number of records that should be in the data_list
    :param test_keys: a set of keys to check with dictionaries in the data_list
    """
    assert len(data_list) == amount, 'Неверное кол-во фильмов в ответе'
    assert type(data_list) is list, 'Тип данных не совпадает'

    # checking types and keys of all received movies
    for record in data_list:

        assert type(record) is dict, 'Тип вложенных данных неверный'
        assert set(record) == test_keys, 'Ключи не совпадают'
