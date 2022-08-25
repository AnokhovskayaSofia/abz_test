from django.db import models


class Employee(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=100)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100)
    patronymic = models.CharField(verbose_name="Отчество", max_length=100)
    image = models.ImageField(verbose_name="Фото работника", upload_to="employees/",
                              blank=True, null=True)
    title = models.CharField(verbose_name="Должность", max_length=100)
    hired_date = models.DateTimeField(verbose_name="Дата приема на работу", blank=True, null=True)
    salary = models.IntegerField(verbose_name="Размер заработной платы", blank=True, null=True)
    parent = models.ForeignKey('self', verbose_name='Начальник', on_delete=models.SET_NULL, blank=True, null=True)