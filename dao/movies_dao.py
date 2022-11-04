"""This unit contains a MovieDao class to work with a movie table"""
from flask_sqlalchemy import SQLAlchemy
# ---------------------------------------------------------------------------


class MovieDao:
    """The MovieDao class provides all necessary logic to work with
    a movie table"""

    def __init__(self, db: SQLAlchemy, model, schema) -> None:
        """Initial method of the MovieDao class

        :param db: the SQLAlchemy instance
        :param model: the Movie class' model
        :param schema: an instance of the Schema class
        """
        self.db = db
        self.model = model
        self.schema = schema

    def get_all(self, page: int = 0) -> tuple:
        """This method returns a list of five movies

        :param page: the page number needed to calculate offset parameter

        :returns:
            movies_list - a list of dicts containing movies data
        """
        # calculating offset parameter
        if page in (0, 1):
            offset = 0

        elif page > 1:
            offset = (page - 1) * 5

        else:
            offset = 0

        session = self.db.session.query(self.model)
        all_movies = session.limit(5).offset(offset).all()

        if not all_movies:
            return 'Not Found', 404

        movies_list = self.schema.dump(all_movies, many=True)

        return movies_list, 200

    def get_by_id(self, movie_id: int) -> tuple:
        """This method returns a dictionary containing data about a movie
        by provided id

        :param movie_id: the id of the searching movie

        :returns:
            movie_dict - a dictionary containing movie data
        """
        movie = self.model.query.get(movie_id)

        if not movie:
            return 'Not Found', 404

        movie_dict = self.schema.dump(movie)

        return movie_dict, 200

    def get_by_director_id(self, director_id: int) -> tuple:
        """This method returns a list of movies found by director_id

        :param director_id: the id of the searching director

        :return:
            movies_list - a list of movies found by director_id
        """
        movies = self.model.query.filter(
            self.model.director_id == director_id).all()

        if not movies:
            return 'Not Found', 404

        movies_list = self.schema.dump(movies, many=True)

        return movies_list, 200

    def get_by_genre_id(self, genre_id: int) -> tuple:
        """This method returns a list of movies found by genre_id

        :param genre_id: the id of the searching genre

        :return:
            movies_list - a list of movies found by genre_id
        """
        movies = self.model.query.filter(self.model.genre_id == genre_id).all()

        if not movies:
            return 'Not Found', 404

        movies_list = self.schema.dump(movies, many=True)

        return movies_list, 200

    def get_by_genre_and_director(self, genre_id: int, director_id: int):
        """This method returns a list of movies found by both genre_id and
        director_id

        :param genre_id: the id of the searching genre
        :param director_id: the id of the searching director

        :returns:
            movies_list - a list of movies found by both genre_id
            and director_id
        """
        movies = self.model.query.filter(self.model.genre_id == genre_id,
                                         self.model.director_id == director_id
                                         ).all()
        if not movies:
            return 'Not Found', 404

        movies_list = self.schema.dump(movies, many=True)

        return movies_list, 200

    def add_new(self, data_dict: dict) -> tuple:
        """This method adds a new movie to the movie table

        :param data_dict: a dictionary containing a new movie data

        :returns:
            a tuple containing the result of the operation
        """
        try:
            new_movie = self.model(**data_dict)
            self.db.session.add(new_movie)
            self.db.session.commit()
            self.db.session.close()
            return 'Created', 201

        except Exception as e:
            print(f'При создании модели возникла ошибка {e}')
            return 'Bad Request', 400

    def update(self, movie_id: int, data_dict: dict) -> tuple:
        """This method updates a movie data

        :param data_dict: a dictionary containing data to update
        :param movie_id: the id of the updated movie

        :returns:
            a tuple containing the result of the operation
        """
        found_movie = self.model.query.get(movie_id)

        if not found_movie:
            return 'Not Found', 404

        try:

            for key in data_dict:

                exec(f'found_movie.{key} = data_dict["{key}"]')

            self.db.session.add(found_movie)
            self.db.session.commit()
            self.db.session.close()

            return '', 204

        except Exception as e:

            print(f'При обновлении данных возникла ошибка {e}')
            return 'Bad Request', 400

    def delete(self, movie_id: int) -> tuple:
        """This method deletes a movie from movie table

        :param movie_id: the id of the deleted movie

        :returns:
            a tuple containing the result of the operation
        """
        found_movie = self.model.query.get(movie_id)

        if not found_movie:
            return 'Not Found', 404

        self.db.session.delete(found_movie)
        self.db.session.commit()
        self.db.session.close()

        return '', 204
