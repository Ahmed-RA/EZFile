from django.shortcuts import render
from django.contrib.auth.models import User
from upload.models import User_extrainfo
from django.contrib.auth import authenticate, logout, login as dj_login
from django.contrib.auth.decorators import login_required
from EZFile.settings import MEDIA_ROOT
from django.db import IntegrityError
from Home import views
from changelog import views as changelog_views
import os

def changelog_view(request):
    renderback = changelog_views.alllogs(request)
    return renderback

def login(request):
    user = request.user
    if user.is_authenticated:
        dir = "Home"
        renderback = views.home_page(request, dir)
        return renderback
    else:
        return render(request, 'login.html', {})


def signup(request):
    user = request.user
    if user.is_authenticated:
        dir = "Home"
        renderback = views.home_page(request, dir)
        return renderback
    else:
        return render(request, 'signup.html', {})

def create_user(request):
    try:
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        user.save()
        path2 = os.path.join(MEDIA_ROOT, str(user.id) )
        os.mkdir(path2)
        user_extrainfo = User_extrainfo.objects.get(usr_id=user)
        user_extrainfo.u_rdir = path2
        user_extrainfo.save()
        return render(request, 'login.html', {"message":"User created, you may login now"})
    except IntegrityError as e:
        return render(request, 'signup.html', {"message":"Something bad happened"})


def authenticate_user(request):
    usernm = request.POST['username']
    pw = request.POST['password']
    user = authenticate(request, username=usernm, password=pw)
    if user is not None:
        dj_login(request, user)
        dir = "Home"
        renderback = views.home_page(request, dir)
        return renderback
    else:
        return render(request, 'login.html', {"message":"Invalid credentials"})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'login.html', {})
