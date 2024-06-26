# Generated by Django 5.0.6 on 2024-06-26 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='orden',
            options={'verbose_name_plural': 'Ordenes'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name_plural': 'Productos'},
        ),
        migrations.AddField(
            model_name='producto',
            name='is_oferta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producto',
            name='oferta_precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
