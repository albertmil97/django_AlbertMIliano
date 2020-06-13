from django import template
from ..models import Reference
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown


register = template.Library()

@register.simple_tag()
def total_references():
    return Reference.objects.count()

@register.inclusion_tag('reference/latest_references.html')
def show_latest_references(count=3):
    latest_references = Reference.objects.order_by('-publish')[:count]
    return {'latest_references': latest_references}