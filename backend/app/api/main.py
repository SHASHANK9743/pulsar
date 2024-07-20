from flask import Blueprint

from backend.app.api.routes import base
from backend.app.api.routes.client import client
from backend.app.api.routes.product import product
from backend.app.api.routes.user import user

api_router = Blueprint("api_router", __name__)

api_router.register_blueprint(blueprint=base.router, )

# client routes for application
api_router.register_blueprint(blueprint=client.router)

# user routes for application
api_router.register_blueprint(blueprint=user.router)

# product routes for applicaton
api_router.register_blueprint(blueprint=product.router)
