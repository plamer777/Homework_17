"""This unit contains a DirectorDao class to work with a director table"""
from flask_sqlalchemy import SQLAlchemy
# --------------------------------------------------------------------------


class DirectorDao:
    """The DirectorDao class provides methods needed to work with the director
    table"""
    def __init__(self, db: SQLAlchemy, model, schema):
        """Initial method of a DirectorDao class

        :param db: a SQLAlchemy class' instance
        :param model: a Director class' model
        :param schema: an instance of the Schema class
        """
        self.db = db
        self.model = model
        self.schema = schema

    def get_all(self) -> tuple:
        """This method returns a list of dictionaries

        :returns:
            a tuple containing a list of dicts or the result of the operation
        """
        all_directors = self.db.session.query(self.model).all()

        if not all_directors:
            return 'Not Found', 404

        directors_list = self.schema.dump(all_directors, many=True)

        return directors_list, 200

    def get_by_id(self, director_id: int) -> tuple:
        """This method returns a dictionary found by the provided id

        :param director_id: the id of a searching record

        :returns:
            a tuple with dictionary and status code or the result of the
            operation instead if record wasn't found
        """
        director = self.model.query.get(director_id)

        if not director:
            return 'Not Found', 404

        director_dict = self.schema.dump(director)

        return director_dict, 200

    def add_new(self, data_dict: dict) -> tuple:
        """This method adds a new record to the table

        :param data_dict: a dictionary containing necessary data

        :returns:
            a tuple containing the result of the operation
        """
        try:

            new_director = self.model(**data_dict)

            self.db.session.add(new_director)
            self.db.session.commit()
            self.db.session.close()

            return 'Added Success', 201

        except Exception as e:

            print(f'Ошибка при добавлении записи {e}')
            return '', 400

    def update(self, record_id: int, data_dict: dict):
        """This method updates a record in the table

        :param record_id: the id of the updating record
        :param data_dict: a dictionary containing necessary data

        :returns:
            a tuple containing the result of the operation
        """
        found_director = self.model.query.get(record_id)

        if not found_director:
            return 'Not Found', 404

        # using exec function instead of filling all fields manually
        for key in data_dict:

            exec(f'found_director.{key} = data_dict["{key}"]')

        self.db.session.add(found_director)
        self.db.session.commit()
        self.db.session.close()

        return '', 204

    def delete(self, record_id: int):
        """This method deletes a record in the table

        :param record_id: the id of the record to delete

        :returns:
            a tuple containing the result of the operation
        """
        found_director = self.model.query.get(record_id)

        if not found_director:

            return 'Not Found', 404

        self.db.session.delete(found_director)
        self.db.session.commit()
        self.db.session.close()

        return '', 204
