# Generated by Django 3.2 on 2021-12-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadro',
            name='imagen',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
