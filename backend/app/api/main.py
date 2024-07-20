from flask import Blueprint

from backend.app.api.routes import base

api_router = Blueprint("api_router", __name__)

api_router.register_blueprint(blueprint=base.router, )
