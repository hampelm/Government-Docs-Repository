from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory

from foialist.models import * 

from foialist.add import *
from foialist.helpers import *

import datetime

    
    
    

class CommentForm(ModelForm):
    poster = forms.CharField()
    
    class Meta:
        model = Comment
    
    
    
    
    
    # HOMEPAGE
    # ======================
def home(request):
    entries = Entry.objects.filter(show=True).order_by("-date_posted")
    return render_to_response('list.html', {'entries': entries})
    
    
    


def thanks(request):
    return render_to_response('thanks.html')
    
    
def about(request):
    return render_to_response('about.html')
    
    
    # DISPLAY DOCS FROM SOURCE
    # ======================
def source(request, sourceid):
    # takes a source ID
    # returns all documents from that source.
    
    entries = Entry.objects.filter(show=True, agency = sourceid).order_by("-date_posted")
    headline = Agency.objects.get(id=sourced).name
    return render_to_response('list.html', {'entries': entries, })
        
    
    # DISPLAY A PAGE BY ID
    # ======================    
def page_by_id(request, pageid):
    try:
        pageid = int(pageid)
    except ValueError:
        raise Http404
        
    try:
        entry = Entry.objects.get(id=pageid)
    except Entry.DoesNotExist:
        return render_to_response('404.html', { 'message' : 'The entry could not be found.'})
        
    return render_to_response('page_by_id.html', {'e': entry})