# Generated by Django 4.0.4 on 2022-05-14 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_foods_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foods',
            name='image',
        ),
    ]
