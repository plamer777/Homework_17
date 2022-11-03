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

    def add_new(self, data_dict: dict):
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
