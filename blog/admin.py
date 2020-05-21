from django.contrib import admin
from .models import Libro

class LibroAmin(admin.ModelAdmin):
    search_fields=['nombre,correo']
   # list_display = ('nombre,poblacion')
    #list_filter=('nombre')

admin.site.register(Libro,LibroAmin)

# Register your models here.
