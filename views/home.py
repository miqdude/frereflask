from flask import Blueprint, render_template
from models import Post

home = Blueprint('home', __name__)

@home.route('/')
def index():
  posts = Post.query.all()
  return render_template("main.html", posts = posts)