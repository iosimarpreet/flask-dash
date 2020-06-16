from flask import Flask, flash, render_template
from web.modules.dog.views import dog_app
from web.modules.cat.views import cat_app
import dash
from web.dash_apps.dog_viz import layout as dog_viz_layout
from web.dash_apps.cat_viz import layout as cat_viz_layout
import logging

server = Flask(__name__)

logging.basicConfig(filename='web.log', level=logging.DEBUG)

# Register your Modules (Apps) here

# Try visiting http://127.0.0.1:5000/dogs/?name=Purri
server.register_blueprint(dog_app, url_prefix="/dogs")
# Try visiting http://127.0.0.1:5000/cats/?name=Meh
server.register_blueprint(cat_app, url_prefix="/cats")

# Register your Dash Apps Here
stylesheets = ['https://cdn.jsdelivr.net/npm/bulma@0.9.0/css/bulma.min.css']

dog_viz = dash.Dash(__name__, server=server, routes_pathname_prefix='/dogs/dog_viz/', external_stylesheets=stylesheets)
dog_viz.layout = dog_viz_layout

cat_viz = dash.Dash(__name__, server=server, routes_pathname_prefix='/cats/cat_viz/', external_stylesheets=stylesheets)
cat_viz.layout = cat_viz_layout


@server.route('/')
def index():
    server.logger.info("Index Route Visited")
    return render_template('index.html')


@server.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    server.logger.info("404 error")
    return render_template('404.html'), 404
