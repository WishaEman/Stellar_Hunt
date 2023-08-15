# Generated by Django 4.2.4 on 2023-08-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('Men', (('polos', 'Polos'), ('casual_shirts', 'Casual Shirts'), ('jeans', 'Jeans'))), ('Women', (('clothes', 'Clothes'), ('shoes', 'Shoes')))], max_length=20, verbose_name='type of category'),
        ),
    ]
