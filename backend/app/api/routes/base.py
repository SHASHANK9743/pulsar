from flask import Blueprint, jsonify

router = Blueprint("base", __name__)


@router.route("/")
def base_route():
    response: dict = dict()
    response["status"] = 200
    response["payload"] = "You have hit the base route of the current Flask Application,"
    return jsonify(response), 200
