"""
Basic Application
"""

import os
from flask import Flask, render_template, request, send_from_directory
from flask.ext.assets import Environment
from webassets.loaders import PythonLoader

app = Flask(__name__, static_folder='static')
assets = Environment(app)


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '')


# Load and register assets bundles.
bundles = PythonLoader('bundles').load_bundles()
for name, bundle in bundles.items():
    assets.register(name, bundle)


@app.route('/')
def home():
    """ Render index """
    return render_template('index.html')


@app.route('/fonts/<path:filename>')
@app.route('/images/<path:filename>')
def serve_static(filename):
    """ Serve up images  """
    dir = request.path[1:].split('/')[0]
    static_path = os.path.join(app.static_folder, dir)
    return send_from_directory(static_path, filename)


@app.route('/robots.txt')
def serve_robots():
    """ Render robots.txt """
    return send_from_directory(app.static_folder, 'robots.txt')


@app.after_request
def add_header(response):
    """
    Add headers to force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(_):
    """Custom 404 page."""
    return render_template('404.html'), 404
