# Generated by Django 4.2.7 on 2023-11-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
    ]
