# Generated by Django 3.2.15 on 2022-08-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo2_app', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='t_img',
            field=models.ImageField(upload_to='t_pics'),
        ),
    ]