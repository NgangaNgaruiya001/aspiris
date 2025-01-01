# Generated by Django 5.1.4 on 2024-12-31 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_salestarget_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdata',
            name='TotalFrgn',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='salestarget',
            name='Month',
            field=models.IntegerField(),
        ),
    ]