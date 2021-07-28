from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('create_user', views.create_user, name='create_user'),
    path('authenticate_user', views.authenticate_user, name='authenticate_user'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('changelog_view', views.changelog_view, name='changelog_view'),
]