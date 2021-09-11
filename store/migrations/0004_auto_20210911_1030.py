# Generated by Django 3.2.7 on 2021-09-11 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210911_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='available_till',
            field=models.DateTimeField(default='2021-10-11 10:30:39.458217'),
        ),
        migrations.AlterField(
            model_name='form',
            name='form_status',
            field=models.CharField(choices=[('LIVE', 'Live'), ('CLOSED', 'Closed'), ('DONE', 'Done'), ('INACTIVE', 'Inactive')], default='INACTIVE', max_length=9),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity_delivered',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
