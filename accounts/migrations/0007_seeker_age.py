# Generated by Django 4.2.1 on 2023-05-09 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_seeker_bio_seeker_profile_image_seeker_short_intro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seeker',
            name='age',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
    ]
