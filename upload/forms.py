from django import forms
from django.forms import ClearableFileInput
from upload.models import UsrUploads, UsrFavfiles

# class UsrUploadsModelForm(forms.ModelForm):
#     class Meta:
#         model = UsrUploads
#         fields = ['upload_dir']
#     #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

# class UsrFavfilesModelForm(forms.ModelForm):
#     class Meta:
#         model = UsrFavfiles
#         fields = ['filename']
#         widgets = {
#             'filename': ClearableFileInput(attrs={'multiple': True}),
#         }
#         # widget is important to upload multiple files