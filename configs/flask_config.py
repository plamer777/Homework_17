"""There is a configuration classes with all necessary settings"""
from os.path import join
# -----------------------------------------------------------------------

# creating OS-independent paths
WORK_PATH = join('..', 'test.db')
TEST_PATH = join('..', 'tests', 'testing.db')
# ------------------------------------------------------------------------


class FlaskConfig:
    """The configuration class for a Flask application"""
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{WORK_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = True
    RESTX_JSON = {'ensure_ascii': False}


class FlaskTestConfig:
    """The configuration class to test a Flask application"""
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{TEST_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = True
    RESTX_JSON = {'ensure_ascii': False}
