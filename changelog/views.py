from Home.views import home_page
from django.shortcuts import render
from .models import Changelog
from user_authent.views import login as home_page_view
 
def alllogs(request):
    logs = Changelog.objects
    return render(request, 'alllogs.html', {'logs':logs})

def homepage_view(request):
    home_page_render = home_page_view(request)
    return home_page_render
