from django.contrib import admin
from .models import Reference

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','link')
    list_filter = ('created','publish','author')
    search_fields = ('title','description')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('publish',)