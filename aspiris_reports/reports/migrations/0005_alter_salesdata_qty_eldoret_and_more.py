# Generated by Django 5.1.4 on 2024-12-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_alter_salesdata_qty_eldoret_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdata',
            name='QTY_Eldoret',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='QTY_Kisumu',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='QTY_Mombasa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='QTY_Nairobi_A',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='QTY_Nairobi_B',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='QTY_Nakuru',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='QTY_Nyeri',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='TOTAL_QTY',
            field=models.FloatField(null=True),
        ),
    ]
