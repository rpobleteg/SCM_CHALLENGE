# Generated by Django 4.1.1 on 2022-10-01 00:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='foundation',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_date', models.DateField(default=datetime.date.today, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.employee')),
            ],
        ),
    ]
