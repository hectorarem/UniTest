"""FireDevs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from FireDevsApp import views
from FireDevsApp.froms import GroupUpdate, GroupDelete, StudentUpdate, StudentDelete

urlpatterns = [
    path('', views.home, name='home'),
    path('group/list/<int:page>', views.group_list, name='group_list'),
    path('group/create', views.group_create, name='group_create'),
    path('group/update/<int:pk>', GroupUpdate.as_view(), name='group_update'),
    path('group/delete/<int:pk>/', GroupDelete.as_view(), name='group_delete'),
    path('student/list/<int:page>', views.student_list, name='student_list'),
    path('student/create', views.student_create, name='student_create'),
    path('student/update/<int:pk>', StudentUpdate.as_view(), name='student_update'),
    path('student/delete/<int:pk>/', StudentDelete.as_view(), name='student_delete'),
    path('reports', views.reports, name='reports'),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('ApiApp.urls'), name="api"),
]
