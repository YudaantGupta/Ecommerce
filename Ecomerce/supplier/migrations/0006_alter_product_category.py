# Generated by Django 4.0.5 on 2022-07-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0005_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Ele', 'Electronics'), ('Clo', 'Clothes'), ('Foo', 'Food'), ('Unc', 'Unclassified')], default='Unc', max_length=50),
        ),
    ]
