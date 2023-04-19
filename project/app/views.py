from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import App, Lista

# Create your views here.



def index(request):
    return render(request, "app/index.html", {
        "app": App.objects.all()
    })

def app(request, app_id):
    compra = App.objects.get(id=app_id)
    print(compra)
    return render(request, "app/pag.html", {
        "app": compra
        
      
    })
