from flask import Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from ..app import db
from ..models.user import User
from ..models.tour_model import Tour
from ..models.merch_model import Merch

admin_page = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

admin = Admin(template_mode='bootstrap3')

# adds the different database models to the Admin panel
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Tour, db.session))
admin.add_view(ModelView(Merch, db.session))