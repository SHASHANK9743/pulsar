from flask import jsonify


def modify():
    response: dict = dict()
    response["status"] = 200
    response["payload"] = "You have hit the product.modify route of the current Flask Application,"
    return jsonify(response), 200
