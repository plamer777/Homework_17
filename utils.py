"""There is a serving function in the unit"""


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
