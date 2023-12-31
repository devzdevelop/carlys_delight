# Generated by Django 4.2.6 on 2023-10-19 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track_inventory', '0002_menuitem_ingredients_unit_reciperequirements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='in_price',
            field=models.FloatField(max_length=0),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='item_price',
            field=models.FloatField(default=0),
        ),
    ]
