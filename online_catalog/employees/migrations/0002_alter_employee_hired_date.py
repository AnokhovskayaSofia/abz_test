# Generated by Django 3.2 on 2022-08-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hired_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата приема на работу'),
        ),
    ]
