# Generated by Django 3.1.3 on 2020-12-07 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitems',
            old_name='content',
            new_name='newcontents',
        ),
    ]
