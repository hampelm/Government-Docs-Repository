from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello world")
    
