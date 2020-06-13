from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Reference(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                                on_delete = models.CASCADE,
                                related_name = 'references' )
    description = models.TextField()
    link = models.URLField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish',)
    def _str_(self):
        return self.title
    def get_absolute_url(self):
        return reverse('reference:reference_detail',
                        args=[self.publish.year,
                                self.publish.month,
                                self.publish.day,
                                self.slug])