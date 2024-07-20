from flask import Blueprint

from backend.app.api.routes.user.register import register

router = Blueprint("user", __name__)
router.add_url_rule("/user/register", view_func=register)
