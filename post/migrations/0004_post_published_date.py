# Generated by Django 2.1.5 on 2020-08-05 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
    ]
