from flask import Blueprint, render_template
from ..models.tour_model import Tour

tour_blueprint = Blueprint("tour_blueprint", __name__, static_folder="static", template_folder="templates")

@tour_blueprint.route("/tour")
def tour_page():
    data = Tour.query.all()
    return render_template("tour.html", data=data)