# Generated by Django 2.1.3 on 2018-12-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20181208_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='imagem',
            field=models.ImageField(default='banner/default.jpg', upload_to='banner/'),
        ),
    ]
