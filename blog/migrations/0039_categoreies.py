# Generated by Django 3.1.1 on 2020-10-01 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_delete_categoreies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoreies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
    ]
