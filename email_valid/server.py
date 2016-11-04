from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form
@app.route('/')
def index():
    emails = mysql.query_db("SELECT * FROM emails")
    print "--------------------------------------------"
    print emails
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    valid = True
    if len(request.form['email']) == 0:
      valid = False
      flash("Email cannot be blank.")
    elif not EMAIL_REGEX.match(request.form['email']):
      valid = False
      flash("Invalid Email Address!")

    if valid:
        session['email'] = request.form['email']
        query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
        data = {'email': request.form['email']}
        mysql.query_db(query, data)
        return redirect('/success')
    else:
      return redirect('/')

@app.route('/success')
def success():
    query = "SELECT * FROM emails ORDER BY created_at DESC"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails)

app.run(debug=True) # run our server