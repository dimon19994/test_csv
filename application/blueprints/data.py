from flask import Blueprint, request

from controllers.data import LoadData, SaveData, ViewData


data = Blueprint("data", __name__)


@data.route("/")
@data.route("/<int:page>")
def view_data(page=1):
    return ViewData(request).call(page)


@data.route("/load_data")
def load_data():
    return LoadData(request).call()


@data.route("/save_data")
def save_data():
    return SaveData(request).call()
