from flask import Blueprint

from backend.app.api.routes.product.add import add
from backend.app.api.routes.product.delete import delete
from backend.app.api.routes.product.fetch import fetch
from backend.app.api.routes.product.modify import modify

router = Blueprint("product", __name__)
router.add_url_rule("/product/add", view_func=add)
router.add_url_rule("/product/delete", view_func=delete)
router.add_url_rule("/product/fetch", view_func=fetch)
router.add_url_rule("/product/modify", view_func=modify)
