# Generated by Django 3.2 on 2022-08-29 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_hired_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hired_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата приема на работу'),
        ),
    ]