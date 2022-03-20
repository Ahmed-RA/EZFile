from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('home_page/<path:dir>', views.home_page, name='home_page'),
    path('upload_page/<path:dir>', views.upload_page, name='upload_page'),
    path('upload_files/<path:dir>', views.upload_files, name='upload_files'),
    path('make_directory/<path:dir>', views.make_directory, name='make_directory'),   
    path('download_file/<path:filename>', views.download_file, name='download_file'),
    path('delete_file/<path:filename>', views.delete_file, name='delete_file'),
]