from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .services import add_vehicle, remove_vehicle, view_cart, checkout_cart, submit_order
from ...models.vehicle import Vehicle

cart_ctrl = Blueprint("cart", __name__)

@cart_ctrl.route("/add/", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        vehicle_id = request.args.get('vehicle_id')
        result = add_vehicle(vehicle_id)
        if result[1] != 200:
            flash(result[0]["message"], "danger")
            return redirect(request.referrer)

    return view_cart()

@cart_ctrl.route("/remove", methods=["GET", "POST"])
def remove():
    if request.method == "POST":
        return remove_vehicle()

    return render_template("cart.html")

@cart_ctrl.route("/cart", methods=["GET", "POST"])
def view():
    return view_cart()

@cart_ctrl.route("/checkout", methods=["GET", "POST"])
def checkout():
    return checkout_cart()

@cart_ctrl.route("/complete_order", methods=["GET", "POST"])
def complete_order():
    return submit_order()