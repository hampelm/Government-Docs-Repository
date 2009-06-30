from foialist.models import *

def entities():
    '''
    builds a list of existing entites
    formatted as a javascript array
    for the autocomplete on the entry form.
    '''
    
    entities = Entity.objects.all()
    entitylist = "["
    for entity in entities:
         entitylist += "\"" + entity.name + "\", "
    entitylist += "]"
    
    return entitylist
