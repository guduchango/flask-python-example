from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest
from app import create_app
from app.forms import LoginForm

app = create_app()

todos = ['Comprar cafe','Enviar solicitud de compra','Entregar video al productor']

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

    context = {
        'user_ip' : user_ip,
        'todos' : todos,
        'login_form': login_form,
        'username': username
        }
    
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('Nombre de usuario registrado correctamente.')
        return redirect(url_for('index'))


    return render_template('hello.html',**context)