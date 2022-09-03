from django.shortcuts import render, redirect
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views import generic
# from haystack.query import SearchQuerySet
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from online_catalog.settings import PAGE_SET_10
from .models import Employee
from .serializer import GetEmployeeSerializer
from .forms import EmployeeForm, SearchForm


class EmployeesListSet(generic.ListView):
    model = Employee
    

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()

    # def all_emloyees(request):
    #     emloyees = Employee.objects.all()
    #     paginator = Paginator(emloyees, PAGE_SET_10)
    #     page_number = request.GET.get("page")
    #     page = paginator.get_page(page_number)
    #     context = {
    #         "page": page,
    #         "paginator": paginator
    #     }
    #     return render(
    #         request,
    #         "all_employees.html",
    #         context
    #     )

    def search_employee(request):
        form = SearchForm()
        cd = []
        results = []
        if 'query' in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                cd = form.cleaned_data
                results = Employee.objects.all().filter((Q(title__icontains=cd['query']) | Q(first_name__icontains=cd['query'])) | 
                                                        (Q(last_name__icontains=cd['query']) | Q(patronymic__icontains=cd['query']))
                                                        )
            cd = cd['query']

        paginator = Paginator(results, PAGE_SET_10)
        page_number = request.GET.get("page")
        page = paginator.get_page(page_number)
        context = {
            "page": page,
            "paginator": paginator,
            'form': form,
            'cd': cd,
        }
        return render(request,
                    'search_employee.html',
                    context)


    def employee_view(request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        context = {
            'employee': employee
        }
        return render(request, 'employee.html', context)

    def employee_edit(request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        form = EmployeeForm(request.POST or None, files=request.FILES or None,
                    instance=employee)

        if not form.is_valid():
            return render(request, "employee_edit.html", {"form": form, "employee": employee, })

        form.save()
        return redirect('employee', pk=pk)


