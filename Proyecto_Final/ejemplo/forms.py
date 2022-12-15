from django import forms
from ejemplo.models import Familiar, Comida, Consola

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

    
class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion','f_nacimiento', 'numero_pasaporte', 'edad']

class ComidaForm(forms.ModelForm):
  class Meta:
    model = Comida
    fields = ['nombre', 'procedencia', 'ingredientes']

class ConsolaForm(forms.ModelForm):
  class Meta:
    model = Consola
    fields = ['nombre', 'tipo', 'color']

    