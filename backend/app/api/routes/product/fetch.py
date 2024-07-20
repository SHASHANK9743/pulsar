from flask import jsonify


def fetch():
    response: dict = dict()
    response["status"] = 200
    response["payload"] = "You have hit the product.fetch route of the current Flask Application,"
    return jsonify(response), 200
