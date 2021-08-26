from django.contrib import messages
from django.forms import ModelForm, widgets
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from FireDevsApp.models import Group, Student


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"
        widgets = {
            "name": widgets.TextInput(attrs={'class': ' form-control'}),
            "capacity": widgets.NumberInput(attrs={'class': ' form-control'}),
            "main_professor": widgets.Select(attrs={'class': ' form-control'}),
        }

class GroupUpdate(UpdateView):
    form_class = GroupForm
    model = Group
    success_url = reverse_lazy('group_list', kwargs={"page": 1})

    def post(self, request, *args, **kwargs):
        messages.success(request, "Grupo modificado con éxito")
        return super(GroupUpdate, self).post(request, *args, **kwargs)

class GroupDelete(DeleteView):
    model = Group
    success_url = reverse_lazy('group_list', kwargs={"page": 1})

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Grupo eliminado con éxito")
        return super(GroupDelete, self).delete(self, request, *args, **kwargs)

class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "name": widgets.TextInput(attrs={'class': ' form-control'}),
            "bornDate": widgets.DateInput(attrs={'class': ' form-control', 'type': 'date'}),
            "email": widgets.EmailInput(attrs={'class': ' form-control'}),
            "gender": widgets.Select(attrs={'class': ' form-control'}),
            "bornCity": widgets.Select(attrs={'class': ' form-control Select2'}),
            "group": widgets.Select(attrs={'class': ' form-control Select2'}),
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        ids = [g.pk for g in Group.objects.all() if g.available()]
        self.fields['group'].queryset = Group.objects.filter(id__in=ids)

class StudentUpdate(UpdateView):
    form_class = StudentForm
    model = Student
    success_url = reverse_lazy('student_list', kwargs={"page": 1})

    def post(self, request, *args, **kwargs):
        messages.success(request, "Estudiante modificado con éxito")
        return super(StudentUpdate, self).post(request, *args, **kwargs)

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list', kwargs={"page": 1})

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Estudiante eliminado con éxito")
        return super(StudentDelete, self).delete(self, request, *args, **kwargs)

