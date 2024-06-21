# Generated by Django 5.0.6 on 2024-06-16 09:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_task_assigneduserid_alter_task_creatoruserid_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='AssignedUserId',
        ),
        migrations.AddField(
            model_name='task',
            name='AssignedUserId',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
