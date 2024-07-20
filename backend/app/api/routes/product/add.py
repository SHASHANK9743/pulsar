from flask import jsonify


def add():
    response: dict = dict()
    response["status"] = 200
    response["payload"] = "You have hit the product.add route of the current Flask Application,"
    return jsonify(response), 200
