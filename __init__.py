from flask import Flask, flash, render_template, request, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from FrereFlask.views import home, post, about, contact
from FrereFlask.models import db


def create_app(test_config=None):
  app = Flask(__name__)
  
  if test_config is None:
    app.config.from_pyfile('config.py')
  
  app.register_blueprint(home)
  app.register_blueprint(post)
  app.register_blueprint(about)
  app.register_blueprint(contact)
  
  db.init_app(app)
  
  return app
