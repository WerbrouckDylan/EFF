from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView
from . import models

# Index view
class IndexView(TemplateView):
    template_name = 'EFF/index.html'

class EmployeeListView(ListView):
    template_name ='EFF/Employees.html'
    model = models.werknemers
