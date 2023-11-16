# Generated by Django 4.2 on 2023-10-14 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_cart_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.CharField(default=datetime.datetime(2023, 10, 14, 8, 21, 18, 19788, tzinfo=datetime.timezone.utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=datetime.datetime(2023, 10, 14, 8, 23, 32, 822773, tzinfo=datetime.timezone.utc), upload_to='uploads'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default=datetime.datetime(2023, 10, 14, 8, 23, 48, 156124, tzinfo=datetime.timezone.utc), upload_to='uploads'),
            preserve_default=False,
        ),
    ]