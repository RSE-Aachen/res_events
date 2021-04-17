from flask import Flask
import models
import os

basedir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
models.db.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)