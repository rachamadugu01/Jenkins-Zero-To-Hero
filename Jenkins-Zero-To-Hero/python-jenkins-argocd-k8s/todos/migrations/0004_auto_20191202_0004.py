# Generated by Django 2.2.7 on 2019-12-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20191202_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(blank=True, verbose_name='Deadline'),
        ),
    ]
