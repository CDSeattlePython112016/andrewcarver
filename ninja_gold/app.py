from flask import Flask, session, redirect, url_for, request, render_template
import random
import time

app = Flask(__name__)

app.secret_key = "ihopethisworks"

def addActivity(num, action, location):
    timestamp = time.strftime("(%Y/%m/%d %I:%M %p)")
    if location == 'casino':
        if action == 'earned':
            earned = 'Earned %d golds from the casino! %s' % (num, timestamp)
            session['activity'].append(['earn', earned])
        elif action == 'lost':
            lost = 'Entered a casino and lost %d golds... Ouch. %s' % (num, timestamp)
            session['activity'].append(['lost', lost])
        else:
            print "error"
    elif location == 'farm':
        session['activity'].append(['earn', 'Earned %d golds from the %s! %s' % (num, location, timestamp)])
    elif location == 'cave':
        session['activity'].append(['earn', 'Earned %d golds from the %s! %s' % (num, location, timestamp)])
    elif location == 'house':
        session['activity'].append(['earn', 'Earned %d golds from the %s! %s' % (num, location, timestamp)])

@app.route('/')
def index():
    if 'ninjagold' not in session:
        session['ninjagold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    return render_template('index.html', activities=session['activity'])

@app.route('/process_money', methods=['POST'])
def goldz():
    if request.form['building'] == 'farm':
        session['farmgold'] = random.randint(10, 20)
        session['ninjagold'] += session['farmgold']
        addActivity(session['farmgold'], 'earned', 'farm')
    elif request.form['building'] == 'cave':
        session['cavegold'] = random.randint(5, 10)
        session['ninjagold'] += session['cavegold']
        addActivity(session['cavegold'], 'earned', 'cave')
    elif request.form['building'] == 'house':
        session['housegold'] = random.randint(2, 5)
        session['ninjagold'] += session['housegold']
        addActivity(session['housegold'], 'earned', 'house')
    elif request.form['building'] == 'casino':
        win_lose = random.randint(0, 1)
        if win_lose == 1:
            session['casinogold'] = random.randint(0, 51)
            addActivity(session['casinogold'], 'earned', 'casino')
            session['ninjagold'] += session['casinogold']
        else:
            session['casinogold'] = random.randint(0, 51)
            addActivity(session['casinogold'], 'lost', 'casino')
            session['ninjagold'] -= session['casinogold']
    return redirect(url_for('index'))

@app.route('/clear')
def clearsession():
    session.clear()
    return redirect('/')

app.run(debug=True)
