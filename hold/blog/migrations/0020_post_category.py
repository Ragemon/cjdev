# Generated by Django 3.2.5 on 2022-02-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20190117_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('blog', 'Blog'), ('song', 'Song'), ('other', 'Other')], default='blog', max_length=20),
        ),
    ]