from django.shortcuts import render
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views import generic

from online_catalog.settings import PAGE_SET_10
from .models import Employee


class EmployeesListSet(generic.ListView):
    model = Employee
    
    def index(request):
        employee_list = Employee.objects.all()
        paginator = Paginator(employee_list, PAGE_SET_10)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        context = {
            'page': page,
            'paginator': paginator
        }
        return render(request, 'index.html', context)
