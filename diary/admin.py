from django.contrib import admin
from .models import Entry, Category, Tag

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created') 
    search_fields = ('title', 'content')
   
    list_filter = () 

   
    exclude = ('category', 'tags', 'video') 
