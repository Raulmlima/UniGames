# Generated by Django 4.2.2 on 2023-06-14 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_alter_cperfil_saldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cperfil',
            name='saldo',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
