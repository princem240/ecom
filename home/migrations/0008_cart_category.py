# Generated by Django 4.2 on 2023-10-14 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_cprice_cart_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]
