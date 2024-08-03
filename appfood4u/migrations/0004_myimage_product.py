# Generated by Django 5.0.4 on 2024-05-21 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfood4u', '0003_myimage_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='myimage',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='appfood4u.product'),
        ),
    ]
