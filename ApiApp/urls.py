from django.urls import path, include
from rest_framework import routers

from ApiApp import views

router = routers.DefaultRouter()
router.register(r'group', views.GroupViewSet, basename="group")
router.register(r'student', views.StudentViewSet, basename="student")

urlpatterns = [
    path('', include(router.urls)),
]