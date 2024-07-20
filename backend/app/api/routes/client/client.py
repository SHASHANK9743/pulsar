from flask import Blueprint

from backend.app.api.routes.client.register import register

router = Blueprint("client", __name__)
router.add_url_rule("/client/register", view_func=register)
