from django import forms

from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'patronymic', 'image', 'title', 'hired_date', 'salary', 'parent')
        label_name = {
            'first_name': 'Имя',
            'last_name' : 'Фамилия',
            'patronymic' : 'Отчество', 
            'image' : 'Фотография',
            'title' : 'Должность',
            'hired_date' : 'Дата наима',
            'salary' : 'Зарплата',
            'parent' : 'Начальник',
        }
        help_texts = {
            'first_name': 'Имя сотрудника',
            'last_name' : 'Фамилия сотрудника',
            'patronymic' : 'Отчество сотрудника',
            'image' : 'Фотография сотрудника',
            'title' : 'Должность сотрудника',
            'hired_date' : 'Дата наима сотрудника',
            'salary' : 'Зарплата сотрудника',
            'parent' : 'Начальник сотрудника',
        }


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск')

