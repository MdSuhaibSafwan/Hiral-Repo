# Generated by Django 4.2.1 on 2023-06-08 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_alter_seeker_knowledge_area_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.knowledgearea'),
        ),
    ]
