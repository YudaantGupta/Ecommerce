# Generated by Django 4.0.5 on 2022-07-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0004_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Ele', 'Electronics'), ('Clo', 'Clothes'), ('Foo', 'Food')], default='unclassified', max_length=50),
        ),
    ]
