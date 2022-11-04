"""The file contains constants to test data received from Flask app"""
import os

# turning on test mode to change flask app settings, this option realized in
# source.py file
os.environ['CURRENT_MODE'] = 'Test'

# test keys
MOVIE_KEYS = {'id', 'title', 'description', 'trailer', 'year', 'rating',
              'genre_id', 'director_id'}

# routes and movies amount to test 'get all' method
ROUTES_GET_ALL = [('/movies/', 5),
                  ('/movies/?page_id=2', 5),
                  ('/movies/?genre_id=16', 3),
                  ('/movies/?director_id=8', 2),
                  ('/movies/?genre_id=18&director_id=8', 1)]

# a dict to test values of received data
VALUES_GET_ONE = {
        "title": "Йеллоустоун",
        "description": "Владелец ранчо пытается сохранить землю своих предков. "
                       "Кевин Костнер в неовестерне от автора «Ветреной реки»",
        "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
        "year": 2018,
        "rating": 8.6,
        "genre_id": 17,
        "director_id": 1,
        "id": 1}

# test data to check POST requests
NEW_MOVIE = {
        "title": "Кошмар на улице Вязов",
        "description": "Раз, два, Фредди заберет тебя",
        "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
        "year": 1980,
        "rating": 8.6,
        "genre_id": 4,
        "director_id": 3,
        "id": 25}

# a test data to check PUT requests
UPDATED_MOVIE = {
        "title": "Больше никаких кошмаров",
        "description": "Фредди ушел и больше не вернется",
        "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
        "year": 2001,
        "rating": 8.6,
        "genre_id": 4,
        "director_id": 3,
        "id": 25
        }
