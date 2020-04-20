from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['userName']
        password = request.POST['password']

        createUser = User.objects.create_user(first_name=name, username=username, password=password)
        createUser.save()
        print("user created")
        return redirect('/')

    else:
        return render(request, 'registration.html')
# Create your views here.
