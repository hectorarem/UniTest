from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from ApiApp.serializers import GroupSerializer, StudentSerializer
from FireDevsApp.models import Group, Student


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    authorization_classes = [TokenAuthentication]
    queryset = Group.objects.all()

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    authorization_classes = [TokenAuthentication]
    queryset = Student.objects.all()
