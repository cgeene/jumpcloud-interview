import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is not None: 
        app.config.from_mapping(test_config)
    elif 'CONFIG_FILEPATH' in os.environ: 
        app.config.from_envvar('CONFIG_FILEPATH')
    else: 
        app.config.from_pyfile('../config/dev_config.py')

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app