# Generated by Django 4.2.1 on 2023-06-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruiter', '0022_alter_dictionary_skill_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]