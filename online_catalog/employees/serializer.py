from django.db.models import F
from django.shortcuts import get_object_or_404
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from .models import Employee

class GetEmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    patronymic = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    image = Base64ImageField(max_length=None, use_url=True)
    salary = serializers.IntegerField(read_only=True)
    hired_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Employee
        fields = ('id',
                  'first_name',
                  'last_name',
                  'patronymic',
                  'title',
                  'image',
                  'salary',
                  'hired_date')
    