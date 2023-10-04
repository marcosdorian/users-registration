from django.shortcuts import render
from .models import User

# home is the name I gave to this view in the urls.py


def home(request):
    return render(request, 'users/home.html')


def users(request):
    newUser = User()
    newUser.name = request.POST.get('name')
    newUser.age = request.POST.get('age')
    # saving info in the database
    newUser.save()
    # showing all registered users in a new page
    users = {
        'users': User.objects.all()
    }

    return render(request, 'users/users.html', users)
