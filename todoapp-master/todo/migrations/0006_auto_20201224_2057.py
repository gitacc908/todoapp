# Generated by Django 3.1.4 on 2020-12-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20201224_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.CharField(max_length=350, unique=True),
        ),
    ]
