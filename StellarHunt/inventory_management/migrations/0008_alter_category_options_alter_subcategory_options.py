# Generated by Django 4.2.4 on 2023-08-09 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0007_alter_category_options_alter_subcategory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['id'], 'verbose_name': 'Subcategory', 'verbose_name_plural': 'Subcategories'},
        ),
    ]
