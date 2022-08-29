from django.shortcuts import render
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views import generic
from rest_framework.pagination import PageNumberPagination

from online_catalog.settings import PAGE_SET_10
from .models import Employee
from .serializer import GetEmployeeSerializer


class EmployeesListSet(generic.ListView):
    model = Employee
    

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()

    def all_emloyees(request):
        emloyees = Employee.objects.all()
        paginator = Paginator(emloyees, PAGE_SET_10)
        page_number = request.GET.get("page")
        page = paginator.get_page(page_number)
        context = {
            "page": page,
            "paginator": paginator
        }
        return render(
            request,
            "all_employees.html",
            context
        )

    def employee_view(request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        context = {
            'employee': employee
        }
        return render(request, 'employee.html', context)

