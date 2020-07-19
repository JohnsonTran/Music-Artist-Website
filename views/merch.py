from flask import Blueprint, render_template
from ..models.merch_model import Merch

merch_bp = Blueprint("merch_bp", __name__, static_folder="static", template_folder="templates")

@merch_bp.route("/merch")
def merch_page():
    data = Merch.query.all()
    dict = categorize(data)
    return render_template("merch.html", data=dict)

# categorizes all the merch items based on type
def categorize(database):
    merch_dict = {}
    for item in database:
        if item.type not in merch_dict:
            merch_dict[item.type] = [item]
        else:
            merch_dict[item.type].append(item)
    return merch_dict