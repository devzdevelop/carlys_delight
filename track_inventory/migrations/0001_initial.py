# Generated by Django 4.2.6 on 2023-10-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default='0')),
                ('in_price', models.FloatField(max_length='0')),
            ],
        ),
    ]