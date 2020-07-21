from flask import Flask, flash, render_template, request, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from views import home, post, about, contact
from models.base import db


if __name__ == '__main__':
  app = Flask(__name__)
  
  app.config.from_pyfile('config.py')
  
  app.register_blueprint(home)
  app.register_blueprint(post)
  app.register_blueprint(about)
  app.register_blueprint(contact)
  
  db.init_app(app)
  
  app.run(debug=True)
