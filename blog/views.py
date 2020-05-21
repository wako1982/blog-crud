from django.shortcuts import render,redirect
from .models import Libro
from .forms import LibroForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'index.html')

@login_required()
def nuevo(request):
    data={
        'form':LibroForm
    }
    if request.method=='POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar')
            
            

    return render(request,'nuevo.html',data)


def listar(request):
    lib = Libro.objects.all()
    data={
        'lib':lib
    }
    return render(request,'listar.html',data)


def modificar(request,id):
    lib = Libro.objects.get(id=id)
    data = {
        'form':LibroForm(instance=lib)
    }
    if request.method=='POST':
        formulario= LibroForm(request.POST,instance=lib)
        if formulario.is_valid():
            formulario.save()
            #data['mensaje']="Editado correctamente"
            return redirect('listar')

    return render(request,'modificar.html',data)
    
    

def eliminar(request,id):
    lib = Libro.objects.get(id=id)
    lib.delete()
     
    return redirect('listar')