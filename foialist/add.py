from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory

from foialist.models import *
from foialist.helpers import *


class FileForm(ModelForm):
    class Meta:
        model = File
        exclude = ('belongs_to')
    
        
class EntryForm(ModelForm):
    
    entity = forms.CharField()
    
    class Meta:
        model = Entry
        exclude = ('slug', 'show', 'date_posted')


    # SUBMIT A DOCUMENT
    # ======================
def add(request):
    
   # EntryFormSet = modelformset_factory(Entry, exclude = ('slug', 'show', 'date_posted'), entity = forms.CharField())
    EntryFormSet = modelformset_factory(Entry, form=EntryForm, exclude = ('slug', 'show', 'date_posted'))
    
    FileFormSet = modelformset_factory(File, form=FileForm, exclude = ('belongs_to'), extra=2)
    
    # DATA IN
    if request.method == "POST":
        entry_formset = EntryFormSet(request.POST, request.FILES, prefix='entries')
        file_formset  = FileFormSet(request.POST, request.FILES, prefix='files')
        
        if entry_formset.is_valid() and file_formset.is_valid():
            
            # entry_formset.save()
            # Changes entity from a string to an Entity object.
            # Creates a new Entity in the DB if the string doesn't match a current entity.
            
            # entry_formset.clean()
    
            entity_name = request.POST['entries-0-entity']
            try:
                entity = Entity.objects.get(name=entity_name)
            except Entity.DoesNotExist:
                entity = Entity(name=entity_name).save()
                
                
            # This uses some annoying trickery to go around the modelformset, because I can't 
            #     figure out how to access modelformset values directly before saving.
            # Will be fairly prone to breakage from naming scheme changes.     
            
           # entry_formset['entries-0-entity'] = entity
            
            
          # this doesn't work either: 
            request.POST['entries-0-entity'] = entity
            entry_formset = EntryFormSet(request.POST, request.FILES, prefix='entries')
            entry = entry_formset.save( commit=False)
            
            entry.date_posted = datetime.datetime.now() 
            
            # show will be used for moderation (to remove questionable documents)
            entry.show = True
            
            entry.save()
            
                
                
            # for file_form in file_formset:
                # run some code
            
            return HttpResponseRedirect('/doc/' + str(entry.id)) 

        else: #form submission is invalid
           
            entitylist = entities()
        
            return render_to_response('add.html', {
                'entryform' : entry_formset, 
                'fileform'  : file_formset,
                'entities'  : entitylist,
                } )
                
   
   # BLANK ENTRY FORM
    else: 
        entry_formset = EntryFormSet(prefix='entries')
        file_formset  = FileFormSet(prefix='files')
        entitylist = entities()
        
        return render_to_response('add.html', {
            'entryform' : entry_formset, 
            'fileform'  : file_formset,
            
            'entities'  : entitylist,
            } )
