from flask import Flask, session, redirect, url_for, request, render_template, flash
import re
import datetime

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[a-zA-Z]+$')
password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')


app = Flask(__name__)

app.secret_key = "ihopethisworks"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    is_valid = True
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    # session['birthday'] = request.form['birthday']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']

    if len(session['email']) == 0 or len(session['first_name']) == 0 or len(session['last_name']) == 0 or len(session['password']) == 0 or len(session['confirm_password']) == 0:
        is_valid = False
        flash("Fields cannot be empty.")

    elif not name_regex.match(session['first_name']) or not name_regex.match(session['last_name']):
        is_valid = False
        flash("Names cannot contain numbers, bozo.")

    # elif datetime.strptime(session['birthdate'], "%m/%d/%Y"):
    #     is_valid = False
    #     flash("Not a valid birthdate.")

    elif not email_regex.match(session['email']):
        is_valid = False
        flash("Not a valid email.")

    elif not password_regex.match(session['password']):
        is_valid = False
        flash("Password must have one captial letter and one number.")

    elif len(session['password']) < 9:
        is_valid = False
        flash("Password must be longer than 8 characters.")

    elif session['password'] != session['confirm_password']:
        is_valid = False
        flash("Passwords should match")

    if is_valid:
        return render_template('result.html')
    else:
        return redirect('/')

app.run(debug=True)
