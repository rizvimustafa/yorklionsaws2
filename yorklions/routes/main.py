from flask import Blueprint, render_template
from ..forms import RegistrationForm, LoginForm

main = Blueprint("main", __name__)

@main.route("/home")
@main.route("/")
def main_index():
    return render_template("index.html")

@main.route("/shop/")
def shop():
    return render_template("index.html")

@main.route("/new-cars/")
def new_cars():
    return render_template("index.html")

@main.route("/reviews/")
def reviews():
    return render_template("index.html")

@main.route("/trade-in/")
def trade_in():
    return render_template("index.html")

@main.route("/hot-deals/")
def hot_deals():
    return render_template("index.html")

@main.route("/admin/", methods=["GET", "POST"])
def admin_dash():
    return render_template("admin.html")
