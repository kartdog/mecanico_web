# Generated by Django 5.0.6 on 2024-06-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_compra_compraproducto_compra_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
