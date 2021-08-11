from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from upload.models import  UsrFavfiles, UsrUploads,  Usr_dirs, User_extrainfo
from django.contrib.auth.decorators import login_required
from EZFile.settings import MEDIA_ROOT, BASE_DIR
import mimetypes
import os
from pathlib import Path



#returns upload page with corresponding selcted directory as the upload destination
@login_required
def upload_page(request, dir):
    upload_dir = dir
    return render(request, 'upload.html', {"dir":upload_dir})



#returns home page with home directory selected
@login_required
def home_page(request, dir, message=None):
    user = request.user
    if dir=="Home":
        path = os.path.join(MEDIA_ROOT, str(user.id)) #initial formating for a user directory       
        scanned_files = os.scandir(path) #get all files in a user directory
        scanned_files_array = [] #used to populate with all files scanned
        scanned_dirs_array = []  #used to populate with all folders found 
    else:
        dir_split = dir.split('/')
        dir_split[0] = str(user.id)
        current_dir = '/'.join(dir_split)
        path = os.path.join(MEDIA_ROOT, current_dir) #initial formating for a user directory       
        scanned_files = os.scandir(path) #get all files in a user directory
        scanned_files_array = [] #used to populate with all files found
        scanned_dirs_array = []  #used to populate with all folders found 
        
    for f in scanned_files:
        rel_path = f.path
        rel_path = rel_path.replace(MEDIA_ROOT,"")
        rel_path = rel_path.replace("\\",r"/") #for files, format the path of each file such that it is the same as in the DB
        if f.is_file():              
            scanned_files_array.append(rel_path)
        else:
            rel_path = rel_path.split('/')
            rel_path[0] = "Home"
            dir_name_for_url = '/'.join(rel_path)
            dir_dict = {"dir_name_for_url" : dir_name_for_url, "dir_name": rel_path[-1]}
            scanned_dirs_array.append(dir_dict)

    
    breadcrumb_list = []
    dir_tree = dir.split('/')
    for idx, single_dir in enumerate(dir_tree):
        if idx == 0:
            breadcrumb_name_for_url = single_dir
        elif idx == len(dir_tree)-1:
            breadcrumb_name_for_url = '/'.join(dir_tree)
        else:
            breadcrumb_name_for_url = '/'.join(dir_tree[0:idx+1])
        breadcrumb_dict = {"breadcrumb_name_for_url" : breadcrumb_name_for_url, "breadcrumb_name": single_dir}
        breadcrumb_list.append(breadcrumb_dict)


    try:
        files_in_dir = UsrFavfiles.objects.filter(filename__in=scanned_files_array) #retrieve objects from the DB table that have the corresponding paths
    except Exception:
        message = "Service was unable to retrieve any files :("
        return render(request, 'Home.html', {"dir":"Home","message":message}) 

    return render(request, 'Home.html', {"dir":dir, "files": files_in_dir, "folders": scanned_dirs_array, 
    "breadcrumb_list": breadcrumb_list, "message": message})



#processes and uploads files from POST request
@login_required
def upload_files(request, dir):
    if request.method == 'POST':
        listfiles = request.FILES.getlist('files[]')
        user = request.user  
        if dir=="Home":
            upload_ds = '' + str(user.id) + '/'
        else:
            dir_split = dir.split('/')
            dir_split[0] = str(user.id)
            current_dir = '/'.join(dir_split)
            upload_ds = '' + current_dir + '/'
        temp_instance = UsrUploads(user_id_for_UsrUploads = user, upload_dir= upload_ds)       
        temp_instance.save()
        for f in listfiles:
            file_instance = UsrFavfiles()
            file_instance.up_ds = upload_ds
            file_instance.filename = f
            file_instance.upload_id = temp_instance
            file_instance.save()
        #return render(request, 'Home.html', {"dir":"Home","upload_message":"files uploaded successfully"})
        render_home_page = home_page(request, dir, "files uploaded successfully")
        return render_home_page





#creates new folder/directory under current directory
@login_required
def make_directory(request, dir):
    if request.method == 'POST':
        user = request.user
        new_directory_name = request.POST["directory"]
        if dir=="Home":
            path = os.path.join(MEDIA_ROOT, str(user.id), new_directory_name)
            os.mkdir(path)
            database_entry = Usr_dirs.objects.create(user_id=user, u_dir = str(user.id) + '/' + new_directory_name)
        else:
            dir_split = dir.split('/')
            dir_split[0] = str(user.id)
            current_dir = '/'.join(dir_split)
            path = os.path.join(MEDIA_ROOT, current_dir, new_directory_name)
            os.mkdir(path)
            database_entry = Usr_dirs.objects.create(user_id=user, u_dir = current_dir + new_directory_name)      
        database_entry.save()
        render_home_page = home_page(request, dir, "new folder created successfully")
        return render_home_page
        #return render(request, 'Home.html', {"dir":"Home","upload_message":"new folder created successfully"})



#retrives a url to download a specific file
def download_file(request, filename):
    #using user extra info query to get the absolute path of the media folder
    user = request.user
    user_extrainfo = User_extrainfo.objects.get(pk=user.id)
    user_absolute_path = user_extrainfo.u_rdir
    user_absolute_path = user_absolute_path.replace("\\",r'/') 
    user_absolute_path = user_absolute_path.split('/')
    path = '/'.join(user_absolute_path[0:-1]) + filename.replace("/media","")    
    file_to_be_downloaded = open(path, 'rb')
    mime_type, _ = mimetypes.guess_type(path)
    response = HttpResponse(file_to_be_downloaded, content_type=mime_type)
    #response['Content-Disposition'] = "attachment; filename=%s"%filename
    return response

#deletes a specific file
@login_required
def delete_file(request, filename):
    #using user extra info query to get the absolute path of the media folder
    user = request.user
    user_extrainfo = User_extrainfo.objects.get(pk=user.id)
    user_absolute_path = user_extrainfo.u_rdir
    user_absolute_path = user_absolute_path.replace("\\",r'/') 
    user_absolute_path = user_absolute_path.split('/')
    path = '/'.join(user_absolute_path[0:-1]) + filename.replace("/media","")  
    filename_in_DB = path.replace('/'.join(user_absolute_path[0:-1]) + '/',"")
    try: 
        os.remove(path)
        file_to_be_deleted = UsrFavfiles.objects.filter(filename__in=filename_in_DB)
        file_to_be_deleted.delete()
    except Exception:
        render_home_page = home_page(request, "Home", "error on file deletion")
        return render_home_page
    filename_in_message = filename.split('/')
    filename_in_message = filename_in_message[-1]
    dir_to_home_page = filename.replace('/media/' + str(user.id), "Home")
    dir_to_home_page = dir_to_home_page.split('/')
    dir_to_home_page = '/'.join(dir_to_home_page[0:-1])
    render_home_page = home_page(request, dir_to_home_page, "file " + filename_in_message + " deleted successfully")
    return render_home_page

        




