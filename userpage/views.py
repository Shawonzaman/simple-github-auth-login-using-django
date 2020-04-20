from django.contrib import auth
from django.shortcuts import render, redirect
from .models import RepoList


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')


def repos(request):
    if request.method == 'GET':
        repo = request.GET.get('repo')
        repos, created = RepoList.objects.get_or_create(repo=repo)
        repos.save()
        print(repo)
        if not repo:
            return render(request, 'userpage.html')
        else:
            return render(request, 'githook.html')
