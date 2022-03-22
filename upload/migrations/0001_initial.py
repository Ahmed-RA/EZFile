# Generated by Django 3.2.2 on 2022-03-20 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import upload.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_extrainfo',
            fields=[
                ('usr_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('utype', models.IntegerField(default=1)),
                ('u_rdir', models.CharField(default='notset', max_length=255)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UsrUploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_dir', models.CharField(default='notset', max_length=255)),
                ('user_id_for_UsrUploads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UsrFavfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.FileField(upload_to=upload.models.get_upload_destination)),
                ('favor', models.BooleanField(default=False)),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.usruploads')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usr_dirs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_dir', models.CharField(default='notset', max_length=255)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'unique_together': {('user_id', 'u_dir')},
            },
        ),
    ]