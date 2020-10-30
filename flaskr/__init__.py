import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is not None:
        app.config.from_mapping(test_config)
    elif "CONFIG_FILEPATH" in os.environ:
        app.config.from_envvar("CONFIG_FILEPATH")
    else:
        raise Exception("Must provied a value for CONFIG_FILEPATH")

    from . import db

    db.init_app(app)

    from . import users

    app.register_blueprint(users.bp)

    return app
