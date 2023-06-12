from django.shortcuts import render
from .models import Estudiante
from django.views.generic import ListView
# Create your views here.


# create a class based list view for model Estudiante
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'miapp/estudiante_list.html'
    context_object_name = 'estudiantes'
    ordering = ['nombre']
    paginate_by = 10

