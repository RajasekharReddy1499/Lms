from django.contrib import admin

# Register your models here.
from Libraryapp.models import *

admin.site.register(Books)
admin.site.register(Course)
admin.site.register(Student)
