# Generated by Django 3.1.4 on 2022-03-09 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moto',
            name='Type',
            field=models.CharField(choices=[('BAJAJ', 'BAJAJ'), ('MOTO', 'MOTO')], max_length=80),
        ),
    ]
