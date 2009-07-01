from django.conf.urls.defaults import *
from foia.views import *
from foialist.views import * 
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', home),
    ('^add/$', add),
    ('^submit/thanks/$', thanks),
    (r'^doc/(\d+)/$', page_by_id),
    
 #  (r'^created/$', by_creation_date),
 #  (r'^submitted/$', by_submission_date),
    
    
    (r'^origin/$', origins),
    (r'^origin/(?P<slug>[-\w]+)/$', by_origin),
    
    (r'^submitter/$', posters),
    (r'^submitter/(?P<slug>[-\w]+)/$', by_poster),
    
    
    
    (r'^admin/(.*)', admin.site.root),
    (r'^templates/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/Users/matth/Projects/foia/templates'})
    # add urls for /year/month
    # can I do one for people without adding another table?
        # I think so -- just convert spaces to underscores for the URL in the view.
        # then back again for the search string 
        # underscores, in case of a hyphenated last name
        # maybe there's mechanism for this already.
)