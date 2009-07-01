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
    
    
    # DISPLAY DOCS by ORIGIN
    # ======================
def origins(request):
    # takes a source ID
    # returns all documents from that source.

    entries = Entity.objects.all()
    
    return render_to_response('entities.html', {'entries': entries, })
    
    
def by_origin(request, slug):
    # takes a source ID
    # returns all documents from that source.
    
    entity = Entity.objects.get(slug=slug)
    entries = Entry.objects.filter(show=True, entity=entity).order_by("-date_posted")
    
    headline = Entity.objects.get(id=entity.id).name
    return render_to_response('list.html', {'entries': entries, })
    
    
    # DISPLAY DOCS by SUBMITTER
    # ======================
    
def posters(request):
    # displays all submitters and the # of contributions.

    posters = Entry.objects.filter(show=True)
    distinct_posters = Entry.objects.values('poster', 'poster_slug').distinct()
    entries = []
    for distinct_poster in distinct_posters:
        count = Entry.objects.filter(poster = distinct_poster['poster']).count()

        entry = {'slug': distinct_poster['poster_slug'], 'name': distinct_poster['poster'], 'count': str(count)}
        entries.append(entry)
    
    return render_to_response('posters.html', {'entries': entries, })
    
    
def by_poster(request, slug):
    # takes a submitter slug
    # returns all documents from that submitter.

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