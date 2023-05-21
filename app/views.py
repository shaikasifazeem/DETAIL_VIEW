from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,ListView,DetailView,CreateView

from app.models import *


class Home(TemplateView):
    template_name='app/home.html'



class SchoolList(ListView):
    model=School
    context_object_name='SFO'


class School_detail(DetailView):
    model=School
    context_object_name='sclobject'

class Schoolcreate(CreateView):
    model=School
    fields='__all__'




