from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.

class ReferenceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
class Reference(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length=255, default = title)
    description = models.TextField()
    link = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'references')
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    
    referenceList = ReferenceManager()
       
    class Meta:
        ordering = ('created',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('reference_detail', kwargs={'pk': self.id, 'slug':self.slug})
    
    

