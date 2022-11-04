"""The file contains different contains for testing purposes"""

# test keys
KEYS = {'id', 'name'}
GENRE_KEYS = {'id', 'name', 'movies'}
TEST_KEYS = [KEYS, GENRE_KEYS]

# test routes
ROUTES = ['/directors/', '/genres/']
ROUTES_AND_AMOUNTS = [
    ('/directors/', 20),
    ('/genres/', 18)
]

# test dictionaries to add in database
NEW_DIRECTOR = {"name": "Тейлор Шеридан", "id": 1}
NEW_GENRE = {"name": "Комедия", "id": 1, "movies": 'Not Found'}
ADD_RECORDS = [NEW_DIRECTOR, NEW_GENRE]

# a list of directories to build more complex test data
GENRE_AND_DIRECTOR_ADD = [{"name": "Люк Бессон", "id": 21},
                          {"name": "Ужасный ужастик", "id": 19}]
GENRE_AND_DIRECTOR_UPDATE = [{"name": "Вася Пупкин", "id": 21},
                             {"name": "Мега комедия", "id": 19}]

# a complex test data to parametrize
GENRE_AND_DIRECTOR_GET = [(route, record, keys) for route, record, keys in
                          zip(ROUTES, ADD_RECORDS, TEST_KEYS)]
ADD_NEW_DATA = [(route, record, keys) for route, record, keys in
                zip(ROUTES, GENRE_AND_DIRECTOR_ADD, TEST_KEYS)]
UPDATE_DATA = [(route, record, keys) for route, record, keys in
               zip(ROUTES, GENRE_AND_DIRECTOR_UPDATE, TEST_KEYS)]
DELETING = [(route, pk) for route, pk in zip(ROUTES, (21, 19))]
