# Generated by Django 5.1.5 on 2025-01-18 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.DeleteModel(
            name='AdminProfile',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
