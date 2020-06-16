from flask import Blueprint, request, render_template
from .repositories import Dog

dog_app = Blueprint("dog_app", __name__)


@dog_app.route("/")
def dog():
    name = request.args.get("name")
    new_dog = Dog(name=name)
    message = new_dog.bark()
    return render_template("dog/main.html", message=message, age=new_dog.age, name=new_dog.name)