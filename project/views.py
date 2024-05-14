from flask import Blueprint, render_template

bp = Blueprint("views", __name__)

@bp.route("/")
def home():
    return render_template("webapp/home.html")

@bp.route("/contact")
def contact():
    return render_template("webapp/contact.html")