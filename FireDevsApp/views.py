from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from FireDevsApp.froms import GroupForm, StudentForm
from FireDevsApp.models import Group, Student


def home(request):
    return render(request, 'home.html')

def group_list(request, page):
    objects = Group.objects.all()
    groups = paginador(objects, 10, page)
    return render(request, 'FireDevsApp/group_list.html', {'groups': groups})

def group_create(request):
    if request.POST:
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Grupo creado con éxito")
            return HttpResponseRedirect('/group/list/1')
        else:
            messages.error(request, "Error en el formulario")
    else:
        form = GroupForm()
    return render(request, 'FireDevsApp/group_form.html', {'form': form})

def student_list(request, page):
    objects = Student.objects.all()
    students = paginador(objects, 10, page)
    return render(request, 'FireDevsApp/student_list.html', {'students': students})


def student_create(request):
    if request.POST:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante creado con éxito")
            return HttpResponseRedirect('/student/list/1')
        else:
            messages.error(request, "Error en el formulario")
    else:
        form = StudentForm()
    return render(request, 'FireDevsApp/student_form.html', {'form': form})

def reports(request):
    res = {}
    res['report'] = []
    groups = Group.objects.all()
    for g in groups:
        res['report'].append({'group_name': g.name, 'group_student_count': g.countStudent()})
    return render(request, 'FireDevsApp/reports.html', res)


# paginador
def paginador(lista, cant, pagina):
    paginar = []
    for i in lista:
        paginar.append(i)
    paginator = Paginator(paginar, cant)
    try:
        paginar = paginator.page(pagina)
    except PageNotAnInteger:
        paginar = paginator.page(1)
    except EmptyPage:
        paginar = paginator.page(paginator.num_pages)
    return paginar