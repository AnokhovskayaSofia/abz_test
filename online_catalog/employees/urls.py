from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import EmployeesListSet



router = DefaultRouter()
# router.register('employees', EmployeesViewSet, basename='EmployeesViewSet')
urlpatterns = [
    # path('', include(router.urls)),
    path('', EmployeesListSet.as_view(), name='index'),
]