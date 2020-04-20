import json

import requests
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    return render(request, 'home.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is None:
        auth.login(request, user)
        return redirect('/')
    else:
        auth.login(request, user)
        return render(request, 'userpage.html')


def git(request):
    response = requests.get('https://api.github.com/users/shawonzaman/repos')
    repodata = response.json()
    print(repodata)
    repos = []
    for repo in repodata:
        repos.append(repo['html_url'])

    return render(request, 'gitpage.html', context={'repos': repos})
