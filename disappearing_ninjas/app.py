from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)

app.secret_key = "ihopethisworks"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def tmnt():
    turturs = True
    return render_template('ninja.html', turturs=turturs)

@app.route('/ninja/<color>')
def ninja(color):
    turturs = False
    return render_template('ninja.html', color=color, turturs=turturs)
    
app.run(debug=True)
