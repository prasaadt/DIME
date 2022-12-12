from django.contrib import admin
from faculty.models import Faculty

# Register your models here.

class facultyadmin(admin.ModelAdmin):
    list_display = ['fno','Fname','Flastname','Fdes']

admin.site.register(Faculty,facultyadmin)