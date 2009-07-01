from django.db import models

class Entity(models.Model):
    name = models.CharField(max_length=150) 
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name
        
        
class Reason(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    
    def __unicode__(self):
        return self.name
    
    
class Entry(models.Model):
    
    helptext = "Add any relevant details about the documents. What are the documents about? Were there any problems or revelations? If your request was denied, what reason was given? What is the larger issue?"    
    
    
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    narrative = models.TextField(default=helptext)
        
    entity = models.ForeignKey(Entity)
    reason = models.ForeignKey(Reason) 
    
    date_filed= models.DateField(
        "Date received", 
        blank=True, 
        null=True, 
        help_text='(optional)' 
        ) 
    date_requested = models.DateField(
        "Date requested",
         blank=True, 
         null=True,
         help_text="(optional)"    
         )
    date_posted = models.DateTimeField(auto_now=True)
    
    #should I do a separate table for submitters? I don't think so
    poster = models.CharField("Your name", max_length=100)
    poster_slug = models.SlugField()
    email  = models.EmailField("Your email")
    
    show = models.BooleanField()
    
    def __unicode__(self):
        return self.title;
    
    
class File(models.Model):
    theFile = models.FileField("File", upload_to='uploaded_files/%Y/')
    belongs_to = models.ForeignKey(Entry)


class Comment(models.Model):
    poster = models.CharField(max_length=100)
    email  = models.EmailField()
    date_posted = models.DateTimeField(auto_now=True)
    body = models.TextField()
    visible = models.BooleanField()
    
    belongs_to = models.ForeignKey(Entry)
    
    def __unicode__(self):
        return u'%s \n %s \n %s' (self.poster, self.date_posted, self.body)