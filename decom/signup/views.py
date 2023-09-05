from django.shortcuts import render
from .serializers import studentserializer
from .models import student
from rest_framework import viewsets

class studentModelviewset(viewsets.ModelViewSet):
  queryset=student.objects.all()
  serializer_class=studentserializer
