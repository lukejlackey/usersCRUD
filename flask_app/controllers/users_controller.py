from flask_app import app
from flask_app.models.users_model import User
from flask import render_template, redirect, request

@app.route('/users')
def displayUsers():
    return render_template('readAll.html', users= list(User.showAll()))

@app.route('/users/<int:id>')
def viewUser(id):
    return render_template('userPage.html', user= User.showUser(id))

@app.route('/users/process', methods=['POST'])
def addUser():
    new_user = request.form
    User.addNewUser(new_user)
    return redirect('/users')

@app.route('/users/<int:id>/process', methods=['POST'])
def editUser(id):
    edits = request.form
    User.editExistingUser(id, edits)
    return redirect(f'/users/{id}')

@app.route('/users/new')
def displayAddUser():
    return render_template('create.html')

@app.route('/users/<int:id>/edit')
def displayEdit(id):
    return render_template('editUser.html', user= User.showUser(id))

@app.route('/users/<int:id>/destroy')
def deleteUser(id):
    User.deleteExistingUser(id)
    return redirect('/users')