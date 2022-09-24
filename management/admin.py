from django.contrib import admin
from .models import Book, Member

# Register your models here.
admin.site.register(Member)
admin.site.register(Book)
