from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from authAppExample.models import Account
from authAppExample.forms import InmuebleForm, CustomCreationForm
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
    messages.success(request, '¡Inmueble creado con exito!' )
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
    messages.success(request, '¡Inmueble editado con exito!' )
    return render(request,'crear_inmueble.html',contexto)

def eliminarInmueble(request,id):
    inmueble = Account.objects.get(id =id)
    inmueble.delete()
    messages.success(request, '¡Inmueble eliminado con exito!' )
    return redirect('perfil')

def perfil(request):
    inmuebles = Account.objects.all()
    contexto ={
        'inmuebles':inmuebles
    }
    return render(request,'perfil.html',contexto)

def hoteles(request):
    return render(request,'hotel.html')

    
def hostales(request):
    return render(request,'hostal.html')

    
def resorts(request):
    return render(request,'resort.html')


def register(request):
   
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():      
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario{username}creado')
            return redirect('index')
    else: 
        form = CustomCreationForm() 
    context = {'form':form}
        #data['form'] = formulario

    return render(request,'registration/registro.html',context)
