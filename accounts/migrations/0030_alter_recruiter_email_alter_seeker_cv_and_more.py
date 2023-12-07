# Generated by Django 4.2.1 on 2023-05-15 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_alter_seeker_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='email',
            field=models.EmailField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='cv',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='email',
            field=models.EmailField(blank=True, max_length=500, null=True, unique=True),
        ),
    ]
