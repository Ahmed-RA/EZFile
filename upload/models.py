from EZFile.settings import DEFAULT_AUTO_FIELD
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django import forms
from django.forms import ClearableFileInput
from allauth.account.signals import user_signed_up
from EZFile.settings import MEDIA_ROOT
import os


class User_extrainfo(models.Model):
    usr_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    utype = models.IntegerField(default=1)
    u_rdir = models.CharField(default="notset",max_length=255)

    def __str__(self):
        return [self.usr_id, self.utype, self.u_rdir]
    class Meta:
        managed = True

def get_upload_destination(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<id>/<filename>
    return '/'.join([instance.up_ds, filename])

class UsrUploads(models.Model):
    user_id_for_UsrUploads = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_dir = models.CharField(default = "notset",max_length=255)


    class Meta:
        managed = True

class UsrFavfiles(models.Model):
    
    up_ds = ""
    upload_id = models.ForeignKey(UsrUploads, on_delete=models.CASCADE)
    filename = models.FileField(upload_to=get_upload_destination)
    favor = models.BooleanField(default=False)
    def get_file_name(self):
        return os.path.basename(self.filename.name)

    class Meta:
        managed = True

class Usr_dirs(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    u_dir = models.CharField(default = "notset",max_length=255)

    def __str__(self):
        return [self.id, self.u_dir]

    class Meta:
        unique_together = (('user_id', 'u_dir'),)
        managed = True



@receiver(post_save, sender=User)
def create_user_extrainfo(sender, instance, created, **kwargs):
    if created:
        User_extrainfo.objects.create(usr_id=instance)

@receiver(user_signed_up)
def create_socialuser_extrainfo(sender, **kwargs):
    user = kwargs['user']
    path2 = os.path.join(MEDIA_ROOT, str(user.id) )
    os.mkdir(path2)
    user_extrainfo = User_extrainfo.objects.get(usr_id=user)
    user_extrainfo.u_rdir = path2
    user_extrainfo.save()
    #p.save()





class UsrUploadsModelForm(forms.ModelForm):
    class Meta:
        model = UsrUploads
        fields = ['upload_dir']

class UsrFavfilesModelForm(forms.ModelForm):
    class Meta:
        model = UsrFavfiles
        fields = ['filename']
        widgets = {
            'filename': ClearableFileInput(attrs={'multiple': True}),
        }
        # widget is important to upload multiple files 




# class Groups(models.Model):
#     gid = models.AutoField(primary_key=True)
#     gname = models.CharField(max_length=255, blank=True, null=True)
#     ownerid = models.ForeignKey('Users', on_delete=models.DO_NOTHING, db_column='ownerid')

#     def __str__(self):
#         return [self.gid, self.gname, self.ownerid]

#     class Meta:
#         db_table = 'groups'

# class GroupUsrs(models.Model):
#     gid = models.OneToOneField(Groups, on_delete=models.CASCADE, db_column='gid', primary_key=True)
#     usr_id = models.OneToOneField(Users, on_delete=models.CASCADE, db_column='usr_id')

#     def __str__(self):
#         return [self.gid, self.usr_id]

#     class Meta:
#         db_table = 'group_usrs'
#         unique_together = (('gid', 'usr_id'),)






