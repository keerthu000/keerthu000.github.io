# Generated by Django 4.1.7 on 2024-04-23 19:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_alter_project_created_date_alter_todo_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]