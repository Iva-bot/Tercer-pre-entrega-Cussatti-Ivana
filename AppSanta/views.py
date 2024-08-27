from django.shortcuts import render
from django.http import HttpResponse
from AppSanta.models import Cliente, Producto
from AppSanta.forms import ProductoFormulario
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(req):
    return render(req, 'appsanta/padre.html')


@login_required
def productos(req):
    return render(req, 'appsanta/productos.html')

@login_required
def proveedores(req):
    return render(req,'appsanta/proveedores.html')
@login_required

def clientes(req):
    return render(req,'appsanta/clientes.html')

@login_required
def envios(req):
    return render(req,'appsanta/envios.html')


#def cliente_form(request):
     #return render(request, "appsanta/clienteFormulario.html")

def cliente_form(req):

    if req.method == 'POST':
        
           cliente = Cliente(nombre=req.POST['cliente'], email=req.POST['correo'])

           cliente.save()

           return render(req, "AppSanta/index.html")
    
    return render(req, "AppSanta/clienteFormulario.html")



def producto_form_2(request):

      if request.method == "POST":


            miFormulario = ProductoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  producto = Producto(nombre=informacion["producto"], cantidad=informacion["cantidad"])

                  producto.save()

                  return render(request, "AppSanta/index.html")

      else:
            miFormulario = ProductoFormulario()


      return render(request, "AppSanta/producto_formulario_2.html", {"miFormulario": miFormulario})



def busquedaProducto(request):
     return render (request, "AppSanta/busquedaProducto.html")

def buscar(request):
     if request.GET["producto"]:
          cantidad= request.GET['producto']
          producto=Producto.objects.filter(producto_icontwins=producto)
          return render(request, "AppSanta/busquedaProducto.html" , {"producto": producto, "cantidad": cantidad})
     
     else:
          respuesta= "Datos no seleccionados"

     return HttpResponse(respuesta)

def leerProducto(request):
    producto = Producto.objects.all()
    contexto = {"producto": producto}
    return render (request, "AppSanta/leerProducto.html",contexto)



def eliminarProducto(request, producto_nombre):
    producto = Producto.objects.get(nombre=producto_nombre)
    producto.delete()

    producto =Producto.objects.all()
    contexto= {"producto": producto}

    return render (request, "AppSanta/leerProducto.html" , contexto)


def productoFormulario(request):
      print("Entrando en la vista productoFormulario")

      if request.method == "POST":
            print("Solicitud POST recibida")

            miFormulario =ProductoFormulario(request.POST)

            if miFormulario. is_valid():
               print("Formulario válido")

               informacion =miFormulario.cleaned_data
               producto= Producto (nombre= informacion ['nombre'], cantidad=informacion['cantidad'])
               producto.save()

               return render (request, "AppSanta/padre.html")
            else:
               print("Formulario no válido")


      else:
        print("Solicitud GET recibida")    
        miFormulario = ProductoFormulario()


      return render(request, "AppSanta/productoFormulario.html", {"miFormulario": miFormulario})



