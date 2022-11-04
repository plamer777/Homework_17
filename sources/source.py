"""This unit contains flask and database instances"""
import os
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from configs.flask_config import FlaskConfig, FlaskTestConfig
from schemas.db_schemas import MovieSchema, DirectorSchema, GenreSchema
# --------------------------------------------------------------------------

# creation of the Flask and SQLAlchemy instances
app = Flask(__name__)
# the test mode is activated when the tests are run
if os.environ.get('CURRENT_MODE') == 'Test':
    app.config.from_object(FlaskTestConfig)

else:
    app.config.from_object(FlaskConfig)

db = SQLAlchemy(app)

# creation of the REST API and Namespace instances
api = Api(app)

# creation of the Schema instances
movie_schema = MovieSchema()
director_schema = DirectorSchema()
genre_schema = GenreSchema()
