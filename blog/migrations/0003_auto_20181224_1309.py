# Generated by Django 2.1.4 on 2018-12-24 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181224_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='updatea',
            new_name='update',
        ),
    ]
