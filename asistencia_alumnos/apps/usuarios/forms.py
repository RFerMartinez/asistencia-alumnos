from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from apps.usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm

'''
Para darle estilos a los formularios (como si fuese en html y css), se lo puede especiicar a los constructores de cada campo
se lo pudede especificar clases que quiero que tenda, se lo hace a travez de un widget
'''

class FormularioRegistro(forms.Form):
    username = forms.CharField(label='Nombre se usuario')
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    last_name = forms.CharField()

# class FormularioRegistroUsuario(forms.ModelForm):
#     pass

class FormularioRegistroUsuario(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    # password = forms.CharField(
    #     widget=forms.PasswordInput(attrs={
    #         'class': 'form-control',
    #     })
    # )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
    password2 = forms.CharField(
        label="Repita contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
    '''
    Por ejemplo, el atributoo 'password' no se inicializó, pero, en la clase FormularioRegistroUsuario() se le dijo que
    va a estar basado en un modelo (forms.ModelForm) --> se establece cual es el modelo con la clase meta
    class Meta: --> model = Usuario. También se establece los campos necesarios con 'fields'
    En apps/usuarios/models.py se declara la tabla Usuario
    '''
    class Meta:
        model = Usuario
        # Ahora le tengo que decir que campos usar.. si puede utilizar todos.. o que campos NO utilizar...
        fields = ['username', 'first_name', 'last_name', 'email'] # '__all__' #Quiere decir que use todos loc campos o que use solo el campo 'username'
        # exclude = ['password']

    def __init__(self, *args, **kwargs):
        super(FormularioRegistroUsuario, self).__init__(*args, *kwargs)

        # print("Estoy en el constructor del formulario")
        # print(f"self.fields --> {self.fields}")
        # Aquí puedo cambiar los valores, por ejemplo el campo 'password'
        # print(self.fields['password'].widget.attrs) # --> {'maxlength': '128'}
        self.fields['email'].widget.attrs['class'] = 'form-control'

