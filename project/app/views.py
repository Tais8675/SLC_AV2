from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import App, Lista
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def adicionar_produto(request):
    if request.method == 'POST':
        # Extrai os dados do POST
        nome = request.POST.get('nome')
        valor = request.POST.get('valor')
        print(nome, valor)  # Adicionado para depuração

        # Salva o produto no banco de dados
        produto = App(nome=nome, valor=valor)
        produto.save()

        # Retorna uma resposta JSON
        return JsonResponse({'status': 'ok'})
    else:
        # Retorna uma resposta de erro caso o método HTTP não seja POST
        return JsonResponse({'status': 'error', 'message': 'Método não permitido'})


##



    


##


def lista(request):
    context = {}
    context['app'] = App.objects.all()

    for app in context['app']:
        app.preco_total = sum(item.preco for item in app.lista.app_set.all())

    return render(request, 'app/app.html', context)

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




def pag(request):
    return render(request, 'app/pag.html')


def inicio(request):
    return render(request, "app/inicio.html")

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'app/cadastro.html')
    
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        usuario = User.objects.filter(username=nome).first()
        if usuario:
            return HttpResponse(f'Usuário ja existe {nome}')
        
        usuario = User.objects.create_user(username=nome, password=senha)
        usuario.save()
        return HttpResponse(f'Usuário {nome} salvo com sucesso')
    

def logar(request):
    if request.method == 'GET':
        return render(request, 'app/logar.html')
    
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        usuario = authenticate(username=nome, password=senha)

        if usuario:
            login(request, usuario)
            return HttpResponse('Usuario autenticado')
        

        else:
            return HttpResponse('Login ou Senha invalidos')
        

@login_required(login_url='/logar')
def pagina(request):
    return HttpResponse('Página...')