# Generated by Django 4.2.1 on 2023-05-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_seeker_cv_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
