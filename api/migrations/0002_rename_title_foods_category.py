# Generated by Django 4.0.4 on 2022-05-14 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foods',
            old_name='title',
            new_name='category',
        ),
    ]
