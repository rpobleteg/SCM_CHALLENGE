# Generated by Django 4.1.1 on 2022-10-01 01:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_mark_mark_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='mark_date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]