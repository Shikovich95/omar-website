# Generated by Django 3.1.1 on 2020-09-27 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_post_categorey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categorey',
        ),
    ]
