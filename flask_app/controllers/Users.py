from flask_app import app
from flask_app.models.User import User
from flask_app.models.Post import Post


from flask import render_template , request, redirect, session


@app.route('/')
def login_registration():
    if 'user_id' in session: 
        return redirect('/bright_ideas')
    return render_template('login_registration.html')


@app.route('/register' , methods = ['POST'])
def register():
    data = request.form
    if User.validate_register(data):
        User.register(data)
    return redirect('/')

@app.route('/login' , methods = ['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        user = User.get_by_email(data)
        session['user_id'] = user.id
        return redirect('/bright_ideas') #--- redirecting to the bright_ideas
    return redirect('/bright_ideas')

@app.route('/bright_ideas')
def bright_ideas():
    if not 'user_id' in session:
        return redirect('/')
    user_data = {'id': session['user_id']}
    user = User.get_by_id(user_data)
    posts = Post.get_all()
    return render_template('bright_ideas.html' , logged_user = user , posts = posts)

@app.route('/user/account')
def account():
    user_data = {'id': session['user_id']}
    user = User.get_by_id(user_data)
    posts = Post.get_by_user_id(user_data)
    return render_template('user/account.html' , user = user , posts = posts)

@app.route('/user/account' , methods = ['POST'])
def updateuser():
    data = request.form
    if User.validate_update(data):
        User.updateuser(data)
    return redirect('/user/account')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')