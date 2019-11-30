## from django.shortcuts import render
from django.views.generic import TemplateView

# Hello 

class HelloWorldView (TemplateView):
    template_name = 'test.html'

# Create your views here.
