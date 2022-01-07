from django.forms import ModelForm
from .models import listar

class trasacaoforms(ModelForm):
    class Meta:
        model=listar
        fields = ['nome','valor','unidade']