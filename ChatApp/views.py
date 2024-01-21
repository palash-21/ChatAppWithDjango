from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.


User = get_user_model()


def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'index.html', context={'users': users})


def chat(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat.html', context={'users': users})