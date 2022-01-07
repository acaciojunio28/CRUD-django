from django.shortcuts import render,redirect
from .models import listar
from .form import trasacaoforms
# Create your views here.
#from django.http import HttpResponse
#import datetime

def home (request):
    data= {}
    data['litagem']=listar.objects.all()
    return render(request,'home.html',data)


def formulario (request):
    form=trasacaoforms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'form.html',{'form':form})

def update(request,pk):
    transacao=listar.objects.get(pk=pk)
    form=trasacaoforms(request.POST or None,instance=transacao)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form.html', {'form': form})



def delete(request,pk):
    transacao = listar.objects.get(pk=pk)
    transacao.delete()
    return redirect('home')