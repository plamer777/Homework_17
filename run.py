"""This is a main file of the Flask application. There are six CBVs here"""
from sources.source import app, api
from app.movies_blueprint import movie_blueprint, movie_ns
from app.directors_blueprint import director_blueprint, director_ns
from app.genre_blueprint import genre_blueprint, genre_ns
# ----------------------------------------------------------------------

# blueprint registration
app.register_blueprint(movie_blueprint)
app.register_blueprint(director_blueprint)
app.register_blueprint(genre_blueprint)

# adding namespaces linked with blueprints
api.add_namespace(director_ns)
api.add_namespace(movie_ns)
api.add_namespace(genre_ns)
# -------------------------------------------------------------------------


@app.errorhandler(404)
def error_404(error_code):
    """This error handler processes 404 errors

    :param error_code: an error code caught up by the handler
    """
    return f'К сожалению страница не найдена, код ошибки - {error_code}'
# --------------------------------------------------------------------------


if __name__ == '__main__':
    app.run()
