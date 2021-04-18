from flask import Blueprint, jsonify
from .models import *

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/events", methods=["GET"])
def get_all_events():
    return jsonify({"Hello": "World!"})


@bp.route("/events", methods=["POST"])
def create_event():
    return jsonify({"Hello": "World deluxe!"})