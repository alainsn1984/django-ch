from django.contrib import admin
from .models import Book

class Bookadmin(admin.ModelAdmin):
    list_display = ('title','author','price',)
    
    
admin.site.register(Book, Bookadmin)