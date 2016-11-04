from flask import Flask, session, redirect, url_for, request, render_template
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriendsdb')
app.secret_key = "ihopethisworks"

@app.route('/')
def index():
    friends = mysql.query_db('SELECT * FROM friends ORDER BY created_at DESC')
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
    data = {
             'first_name': request.form['first_name'], 
             'last_name':  request.form['last_name'],
             'email': request.form['email']
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    # proccesses the updated friend
    query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email WHERE id=:id;"
    data = {
             'first_name': request.form['first_name'], 
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'id': id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    # Will display the current unedited friend info
    query = "SELECT * FROM friends WHERE id = :id"
    data = {'id': id}
    edit_friend = mysql.query_db(query, data)[0]
    return render_template('edit.html', friend = edit_friend)

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    # from the '/' delete button for each friend
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
