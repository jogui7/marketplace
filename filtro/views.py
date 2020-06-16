from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Anuncio
from .forms import AnuncioForm

# Create your views here.
def index(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'index.html', {'anuncios': anuncios})

def anuncioView(request, id):
    anuncio = get_object_or_404(Anuncio, pk=id)
    return render(request, 'anuncios/anuncio.html', {'anuncio': anuncio})


@login_required
def newAnuncio(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AnuncioForm()
        return render(request, 'anuncios/addanuncio.html' , {'form':form})
