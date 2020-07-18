from flask import Blueprint, render_template, request
from ..models.merch_model import Merch

product_blueprint = Blueprint("product_blueprint", __name__, static_folder="static", template_folder="templates")

@product_blueprint.route("/product")
def product_page():
    id = request.args.get('id', None)
    product = Merch.query.get(int(id))
    return render_template("product.html", product=product)