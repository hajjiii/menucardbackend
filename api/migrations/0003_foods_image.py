# Generated by Django 4.0.4 on 2022-05-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_title_foods_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
