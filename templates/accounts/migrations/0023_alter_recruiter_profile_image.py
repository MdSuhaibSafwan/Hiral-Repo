# Generated by Django 4.2.1 on 2023-05-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_alter_seeker_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='profile_image',
            field=models.ImageField(blank=True, default='user-default.png', null=True, upload_to='images/profile/'),
        ),
    ]
