# Generated by Django 3.0 on 2023-05-04 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]
