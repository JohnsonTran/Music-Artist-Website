from flask import Blueprint, render_template
from flask_login import login_required, current_user

profile = Blueprint('profile', __name__)

@profile.route('/profile')
@login_required
def profile_page():
    return render_template('profile.html', name=current_user.name)