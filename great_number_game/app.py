
import random
from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)

app.secret_key = "ihopethisworks"

@app.route('/')
def index():
    session['answer'] = random.randint(1, 101)
    session['try_number'] = 1
    session['guess'] = 0
    return redirect(url_for('guess'))

@app.route('/process', methods=['POST'])
def process():
    session['guess'] = int(request.form['guess']) if 'guess' in request.form else None
    if session['guess'] == session['answer']:
        return render_template('win.html')
    else:
        session['try_number'] += 1
    return redirect(url_for('guess'))

@app.route('/guess')
def guess():
    return render_template('guess.html')

if __name__ == '__main__':
    app.run(debug=True)
