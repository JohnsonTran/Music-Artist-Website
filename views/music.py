from flask import Blueprint, render_template

music_bp = Blueprint("music_bp", __name__)

@music_bp.route("/music")
def music_page():
    return render_template("music.html")