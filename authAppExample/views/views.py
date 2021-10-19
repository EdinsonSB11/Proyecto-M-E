from django.shortcuts import render,redirect
from authAppExample.models import Account
from authAppExample.forms import InmuebleForm, UserRegisterForm
from django.contrib import messages

def inicio(request):
    inmuebles = Account.objects.all()
    contexto ={
        'inmuebles':inmuebles
    }
    return render(request,'index.html',contexto)


def crearInmueble(request):
    if request.method == 'GET':
        form = InmuebleForm()
        contexto = {
            'form':form
        }
    else:
        form = InmuebleForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('perfil')
    return render(request,'crear_inmueble.html',contexto)

def editarInmueble(request,id):
    inmueble = Account.objects.get(id = id)
    if request.method == 'GET':
        form = InmuebleForm(instance = inmueble)
        contexto = {
            'form':form
        }
    else:
        form = InmuebleForm(request.POST,instance=inmueble)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('perfil')
    return render(request,'crear_inmueble.html',contexto)

def eliminarInmueble(request,id):
    inmueble = Account.objects.get(id =id)
    inmueble.delete()
    return redirect('perfil')

def perfil(request):
    inmuebles = Account.objects.all()
    contexto ={
        'inmuebles':inmuebles
    }
    return render(request,'perfil.html',contexto)


def register(request):
    if request.method == 'POST':
	    form = UserRegisterForm(request.POST)
	    if form.is_valid():
		    form.save()
		    username = form.cleaned_data['username']
		    messages.success(request, f'Usuario {username} creado')
		    return redirect('index')
    else:
		    form = UserRegisterForm()

    context = { 'form' : form }
    return render(request, 'registration/registro.html', context)
