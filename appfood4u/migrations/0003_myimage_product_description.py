# Generated by Django 5.0.4 on 2024-05-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfood4u', '0002_rename_products_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='Product1', max_length=100),
        ),
    ]
