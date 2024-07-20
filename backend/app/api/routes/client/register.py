from flask import jsonify


def register():
    response: dict = dict()
    response["status"] = 200
    response["payload"] = "You have hit the client.register route of the current Flask Application,"
    return jsonify(response), 200
