# Generated by Django 2.1.3 on 2018-12-08 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20181208_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='frase',
            field=models.CharField(max_length=40, verbose_name='Frase para o banner inicial'),
        ),
    ]
