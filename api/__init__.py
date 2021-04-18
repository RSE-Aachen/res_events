import os
from flask import Flask
from models import *


def create_app(test_config=None):
    """
    Create and configure the application
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:////"
        + os.path.join(app.instance_path, "database.sqlite"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    create_app()