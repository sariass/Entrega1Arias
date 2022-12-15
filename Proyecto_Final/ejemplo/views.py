from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Comida, Consola
from ejemplo.forms import Buscar, FamiliarForm, ComidaForm, ConsolaForm
from django.views import View

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    return render (request, "ejemplo/saludar_a.html", {"nombre": nombre})

def sumar(request, a, b):
    return render (request, 'ejemplo/sumar.html',
    {"a":a,
     "b":b,
     "resultado": a + b
    }
    )

def buscar(request):
    lista_de_nombre = ["Seba","Intx"]
    query = request.GET['q']
    
    if query in lista_de_nombre:
        indice_de_resultado = lista_de_nombre.index(query)
        resultado = lista_de_nombre[indice_de_resultado]
    else:
        resultado = "no hay match"

    return render(request, 'ejemplo/buscar.html', {"resultado": resultado})

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "f_nacimiento":"","numero_pasaporte":"","edad":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})

def mostrar_comidas(request):
  lista_comidas = Comida.objects.all()
  return render(request, "ejemplo/comidas.html", {"lista_comidas": lista_comidas})

class BuscarComida(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_comida.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_comidas = Comida.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_comidas':lista_comidas})
        return render(request, self.template_name, {"form": form})

class AltaComida(View):

    form_class = ComidaForm
    template_name = 'ejemplo/alta_comida.html'
    initial = {"nombre":"", "procedencia":"", "ingredientes":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la comida {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarComida(View):
  form_class = ComidaForm
  template_name = 'ejemplo/actualizar_comida.html'
  initial = {"nombre":"", "procedencia":"", "ingredientes":""}
  
  def get(self, request, pk): 
      comida = get_object_or_404(Comida, pk=pk)
      form = self.form_class(instance=comida)
      return render(request, self.template_name, {'form':form,'comida': comida})

  def post(self, request, pk): 
      comida = get_object_or_404(Comida, pk=pk)
      form = self.form_class(request.POST ,instance=comida)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito la comida {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'comida': comida,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarComida(View):
  template_name = 'ejemplo/comidas.html'
  
  def get(self, request, pk): 
      comidas = get_object_or_404(Comida, pk=pk)
      comidas.delete()
      comidas = Comida.objects.all()
      return render(request, self.template_name, {'lista_comidas': comidas})

def mostrar_consolas(request):
  lista_consolas = Consola.objects.all()
  return render(request, "ejemplo/consolas.html", {"lista_consolas": lista_consolas})

class BuscarConsola(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_consola.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_consolas = Consola.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_consolas':lista_consolas})
        return render(request, self.template_name, {"form": form})

class AltaConsola(View):

    form_class = ConsolaForm
    template_name = 'ejemplo/alta_consola.html'
    initial = {"nombre":"", "tipo":"", "color":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la consola {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarConsola(View):
  form_class = ConsolaForm
  template_name = 'ejemplo/actualizar_consola.html'
  initial = {"nombre":"", "tipo":"", "color":""}
  
  def get(self, request, pk): 
      consola = get_object_or_404(Consola, pk=pk)
      form = self.form_class(instance=consola)
      return render(request, self.template_name, {'form':form,'consola': consola})

  def post(self, request, pk): 
      consola = get_object_or_404(Consola, pk=pk)
      form = self.form_class(request.POST ,instance=consola)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito la consola {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'consola': consola,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarConsola(View):
  template_name = 'ejemplo/consolas.html'
  
  def get(self, request, pk): 
      consolas = get_object_or_404(Consola, pk=pk)
      consolas.delete()
      consolas = Consola.objects.all()
      return render(request, self.template_name, {'lista_consolas': consolas})