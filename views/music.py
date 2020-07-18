from flask import Blueprint, render_template

music = Blueprint("music", __name__, static_folder="static", template_folder="templates")

@music.route("/music")
def music_page():
    return render_template("music.html")