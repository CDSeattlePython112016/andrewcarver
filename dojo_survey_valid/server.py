from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)

app.secret_key = "ihopethisworks"

@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
  if len(request.form['name']) < 1:
    flash("Name cannot be empty!") # just pass a string to the flash function
  elif len(request.form['comment']) > 120:
    flash("Chill we dont want to know that much about you!")
  else:
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template('result.html')
  return redirect('/') # either way the application should return to the index and display the message

app.run(debug=True)              