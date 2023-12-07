# Generated by Django 4.2.1 on 2023-05-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_knowledge_area_alter_seeker_knowledge_area_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='seeker',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seeker',
            name='profile_image',
            field=models.ImageField(blank=True, default='image/profile/user-default.png', null=True, upload_to='images/profile/'),
        ),
        migrations.AddField(
            model_name='seeker',
            name='short_intro',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='seeker',
            name='social_github',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='seeker',
            name='social_linkedin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='seeker',
            name='social_twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='seeker',
            name='social_website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='seeker',
            name='social_youtube',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
