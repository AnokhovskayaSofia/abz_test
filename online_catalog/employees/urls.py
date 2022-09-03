from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import EmployeesListSet, EmployeesViewSet



router = DefaultRouter()
router.register('employees', EmployeesViewSet, basename='one')
urlpatterns = [
    path('search_employee/', EmployeesViewSet.search_employee , name='search_employee'),
    path('', EmployeesListSet.as_view(), name='index'),
    path('<int:pk>/', EmployeesViewSet.employee_view, name='employee'),
    path('<int:pk>/edit/', EmployeesViewSet.employee_edit, name='employee_edit')
]