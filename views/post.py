from flask import Blueprint, render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
import os
from models import Post

post = Blueprint('post', __name__)

UPLOAD_FOLDER = 'static/upload'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@post.route('/post/<postId>')
def viewPost(postId):
  post = Post.query.get(postId)
  return render_template("post.html", post=post)

@post.route('/post/new')
def newPost():
  return render_template("postAdd.html")

@post.route('/post/create', methods=['GET','POST'])
def createPost():
  if request.method == 'POST':
    postTitle = request.form['postTitle']
    postBody = request.form['postBody']
    postSubTitle = request.form['postSubTitle']
    
    if 'postImage' not in request.files:
      flash('No file part')
      return redirect(request.url)
    
    file = request.files['postImage']
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      filenameFullPath = os.path.join(UPLOAD_FOLDER + '/images/', filename)
      file.save(filenameFullPath)
      post = Post(title = postTitle, subTitle = postSubTitle, content = postBody, image = filename)
      Post.session.add(post)
      Post.session.commit()
    
    return redirect(url_for('newPost'))
  
  else:
    return redirect(url_for('newPost'))