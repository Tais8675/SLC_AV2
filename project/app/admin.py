#from django.contrib import admin
#from .models import  App, Lista


#admin.site.register(Lista)
#admin.site.register(App)


from django.contrib import admin
from .models import Lista, App

class AppInline(admin.StackedInline):
    model = App

class ListaAdmin(admin.ModelAdmin):
    inlines = [AppInline]
    list_display = ['nome', 'total']

admin.site.register(Lista, ListaAdmin)
admin.site.register(App)
