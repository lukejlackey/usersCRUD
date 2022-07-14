from flask_app import app
from flask_app.models.users_model import User
from flask import render_template, redirect, request

@app.route('/users')
def displayUsers():
    return render_template('readAll.html', users= list(User.showAll()))

@app.route('/process', methods=['POST'])
def addUser():
    new_user = request.form
    User.addNewUser(new_user)
    return redirect('/users')

@app.route('/users/new')
def displayAddUser():
    return render_template('create.html')
