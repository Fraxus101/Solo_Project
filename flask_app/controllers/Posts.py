from flask_app import app
from flask_app.models.Post import Post
from flask_app.models.User import User

from flask import request , render_template , session , redirect

@app.route('/new')
def add_review():
    user = User.get_by_id({'id': session['user_id']})
    return render_template('new.html', logged_user = user)

@app.route('/add_idea' , methods = ['POST'])
def create():
    data = request.form
    Post.create(data)
    return redirect('/dashboard')

@app.route('/show/<int:id>')
def show_magazine(id):
    post = Post.get_by_id({'id': id})
    return render_template('show.html' , post = post)

@app.route('/review/update' , methods = ['POST'])
def update():
    data = request.form
    Post.update(data)
    return redirect('/dashboard')

@app.route('/account/<int:id>/delete')
def delete(id):
    data = {'id': id}
    review = Post.get_by_id(data)
    if review.user.id == session['user_id']:
        Post.delete(data)
    
    return redirect('/user/account')

@app.route('/review/<int:id>')
def show(id):
    data = {'id': id}
    review = Post.get_by_id(data)
    return render_template('show_review.html' , review = review)

@app.route('/post/<int:id>/like')
def like(id):
    Post.add_user_like({'users_id': session['user_id'] , 'post_id': id})
    return redirect('/dashboard')

@app.route('/post/<int:id>/dislike')
def dislike(id):
    print({'users_id': session['user_id'] , 'post_id': id})
    Post.remove_user_like({'users_id': session['user_id'] , 'posts_id': id})
    return redirect('/dashboard')