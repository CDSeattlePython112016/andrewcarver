from django.shortcuts import render, HttpResponse, redirect
import random, string
def index(request):
    return render(request, "randomword/index.html")

def generate(request):
    if 'attempt' in request.session:
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1
    request.session['word'] = ''.join(random.sample(string.lowercase+string.digits,14))
    return redirect('/')

def reset(request):
	del request.session['attempt']
	del request.session['word']
	return redirect('/')
