from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import EmployeesListSet, EmployeesViewSet



router = DefaultRouter()
router.register('employees', EmployeesViewSet, basename='one')
urlpatterns = [
    path('employees_list', EmployeesViewSet.all_emloyees , name='all_employees'),
    path('', EmployeesListSet.as_view(), name='index'),
    path('<str:pk>/', EmployeesViewSet.employee_view, name='employee'),
    path('<int:pk>/edit/', EmployeesViewSet.employee_edit, name='employee_edit')
]