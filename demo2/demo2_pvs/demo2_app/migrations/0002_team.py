# Generated by Django 3.2.15 on 2022-08-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo2_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=100)),
                ('t_img', models.ImageField(upload_to='pics')),
                ('t_desc', models.TextField()),
            ],
        ),
    ]