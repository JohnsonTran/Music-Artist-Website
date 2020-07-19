from flask import Blueprint, render_template
from ..models.tour_model import Tour

tour_bp = Blueprint("tour_bp", __name__)

@tour_bp.route("/tour")
def tour_page():
    data = Tour.query.all()
    return render_template("tour.html", data=data)