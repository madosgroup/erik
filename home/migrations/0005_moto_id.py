# Generated by Django 3.1.4 on 2022-03-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220310_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='id',
            field=models.CharField(blank=0, default=1, max_length=80, null=0),
            preserve_default=False,
        ),
    ]