# Generated by Django 4.2.1 on 2023-06-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruiter', '0014_alter_jobpost_organaization_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='organaization_logo',
            field=models.ImageField(blank=True, default='jobpost.jpg', null=True, upload_to=''),
        ),
    ]
