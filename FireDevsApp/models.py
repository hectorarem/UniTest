from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from FireDevsApp.validators import MinAgeValidator, MaxAgeValidator, calculate_age

class Gender(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    class Meta:
        db_table = 'sexo'

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    class Meta:
        db_table = 'pais'

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='País')

    class Meta:
        db_table = 'ciudad'

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre', validators=[RegexValidator(r'^[a-zA-Z ]*$', 'Solo letras.')])

    class Meta:
        db_table = 'persona'

    def __str__(self):
        return self.name

class Professor(Person):

    class Meta:
        db_table = 'profesor'

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    main_professor = models.ForeignKey(Professor, on_delete=models.Model)
    capacity = models.IntegerField(verbose_name='Capacidad', default=30)

    class Meta:
        db_table = 'grupo'

    def __str__(self):
        return self.name

    def countStudent(self):
        return self.student_set.all().count()

    def available(self):
        return self.countStudent() < self.capacity


class Student(Person):
    bornDate = models.DateField(verbose_name='Fecha de nacimiento', validators=[MinAgeValidator(18), MaxAgeValidator(27)]) #age range
    email = models.EmailField(verbose_name='Email')
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT, verbose_name='Sexo')
    bornCity = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Ciudad de nacimiento')
    group = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='Grupo')

    class Meta:
        db_table = 'estudiante'

    def __str__(self):
        return self.name

    def age(self):
        return calculate_age(self.bornDate)

    def save(self, *args, **kwargs):
        if self.group.available():
            super(Student, self).save(*args, **kwargs)
        else:
            raise ValueError('Error!, este grupo ya no tiene capacidad.')
