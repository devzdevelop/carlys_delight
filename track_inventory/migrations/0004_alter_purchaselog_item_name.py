# Generated by Django 4.2.6 on 2023-10-20 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('track_inventory', '0003_alter_ingredients_in_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaselog',
            name='item_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track_inventory.menuitem'),
        ),
    ]
