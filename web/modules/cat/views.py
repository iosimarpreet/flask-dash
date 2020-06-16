from flask import Blueprint, request, render_template
from .repositories import Cat

cat_app = Blueprint("cat_app", __name__)


@cat_app.route("/")
def cat():
    name = request.args.get("name")
    new_cat = Cat(name=name)
    message = new_cat.meow()
    return render_template("cat/main.html", message=message, age=new_cat.age, name=new_cat.name)