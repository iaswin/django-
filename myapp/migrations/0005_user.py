# Generated by Django 3.0 on 2023-05-04 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=10)),
                ('LastName', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]