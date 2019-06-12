from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView
from . import models

# Index view
class IndexView(TemplateView):
    template_name = 'EFF/index.html'

class EmployeeListView(ListView):
    context_object_name = 'employeeView'
    template_name ='EFF/Employees.html'
    model = models.werknemer

class EmployeeCreateView(CreateView):
    template_name = 'EFF/createEmployee.html'
    fields = ('personeelsnummer','naam','voornaam','skills','functie')
    model = models.werknemer
    