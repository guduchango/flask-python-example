from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest
from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users,get_todos

app = create_app()

@app.cli.command()
def test():
     # Discover tests in the current directory
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    
    # Create a test runner
    runner = unittest.TextTestRunner()
    
    # Run the tests
    runner.run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response

@app.route('/hello', methods=['GET','POST'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')

    for user in users:
        print(user.id)
        print(user.to_dict()['password'])

    context = {
        'user_ip' : user_ip,
        'todos' : get_todos(user_id=username),
        'username': username
        }
    
    users = get_users()

    for user in users:
        print(user.id)
        print(user.to_dict()['password'])

    

    return render_template('hello.html',**context)