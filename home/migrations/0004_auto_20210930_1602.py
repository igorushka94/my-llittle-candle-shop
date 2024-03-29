# Generated by Django 3.0.3 on 2021-09-30 13:02

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210927_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Покупатель', 'verbose_name_plural': 'Покупатель'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, upload_to=home.models.get_timestamp_path, verbose_name='Изображение'),
        ),
    ]
