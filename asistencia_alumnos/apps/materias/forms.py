from django import forms

from .models import Materia, Categoria

class MateriaForm(forms.ModelForm):
    categorias = forms.ModelMultipleChoiceField(
        queryset= Categoria.objects.all(),
        # widget = forms.CheckboxSelectMultiple,
        widget = forms.SelectMultiple,
    )

    class Meta:
        model = Materia
        fields = ["nombre", "categorias"]