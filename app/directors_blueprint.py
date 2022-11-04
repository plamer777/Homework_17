"""This file contains CBVs to process requests sent to
the '/directors/' route"""
from flask import Blueprint, request
from flask_restx import Api, Resource
from dao.director_dao import DirectorDao
from models.db_models import Director
from sources.source import db, director_schema
# ---------------------------------------------------------------------------

# creating all necessary instances
director_blueprint = Blueprint('director', __name__)
api = Api(director_blueprint)
director_ns = api.namespace('directors')
director_dao = DirectorDao(db, Director, director_schema)
# ---------------------------------------------------------------------------


@director_ns.route('/')
class DirectorsView(Resource):
    """The DirectorsView is a CBV to process routes like '/directors/'"""

    def get(self):
        """This method returns a list of all directors found by the
        '/directors/ route

        :returns:
            a tuple with a result of the request
        """
        result = director_dao.get_all()

        return result

    def post(self):
        """This method serves to process POST requests

        :returns:
            result - a tuple with a result of the POST request
        """
        new_director = request.json

        result = director_dao.add_new(new_director)

        return result


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    """The DirectorView is a CBV to process routes like
    '/directors/1'"""

    def get(self, director_id: int):
        """This method serves to process GET requests for routes like
        '/directors/1'

        :param director_id: the id of the searching director

        :returns:
            a tuple with a result of the request
        """
        result = director_dao.get_by_id(director_id)

        return result

    def put(self, director_id: int):
        """This method serves to process PUT requests

        :param director_id: an id of a record in the table

        :returns:
            result - a tuple with a result of the PUT request
        """
        new_data = request.json

        result = director_dao.update(director_id, new_data)

        return result

    def delete(self, director_id):
        """This method serves to process DELETE requests

        :param director_id: the id of a record in the table

        :returns:
            result - a tuple with a result of the DELETE request
        """
        result = director_dao.delete(director_id)

        return result