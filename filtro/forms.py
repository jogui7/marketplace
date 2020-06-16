from django import forms

from .models import Anuncio

class AnuncioForm(forms.ModelForm):

    class Meta:
        model = Anuncio
        fields = ('title','image','description','shortDescription','price','condition','category')
            