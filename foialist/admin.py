from django.contrib import admin
from foia.foialist.models import *

admin.site.register(File)
admin.site.register(Comment)
admin.site.register(Entry)
admin.site.register(Entity)
admin.site.register(Reason)