from flask import Blueprint, render_template
from ..models.tour_model import Tour

tour_bp = Blueprint("tour_bp", __name__)

@tour_bp.route("/tour")
def tour_page():
    # sorts the tour events by dates no matter the ordering in the database
    data = Tour.query.order_by(Tour.date).all()
    return render_template("tour.html", data=data)