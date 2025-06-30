from django.shortcuts import render
from .models import Post, Producto
from .forms import ProductoFormulario

# Create your views here.
def index( request ):
    context = { "mensaje":"Bienvenido a mi aplicación Django"}
    return render(request,"appTerceraEntrega/index.html", context)

def post_list( request ):
    post_list = Post.objects.all()
    return render(request, "appTerceraEntrega/post_list.html", context={"posts":post_list})

def productos( request ):  
    productos = Producto.objects.all()  
    return render(request, "appTerceraEntrega/productos.html", context={"productos":productos})

def producto_formulario(request):
      if request.method == "POST":
            formulario_producto = ProductoFormulario(request.POST) 
            if formulario_producto.is_valid():
                  datos = formulario_producto.cleaned_data                  
                  
                  if datos["precio"] is None:
                       datos["precio"] = 0
                  
                  if datos["stock"] is None:
                       datos["stock"] = 0

                  nuevo_producto = Producto(codigo_producto=datos["codigo_producto"],descripcion=datos["descripcion"],precio=datos["precio"],stock=datos["stock"],activo=datos["activo"])
                  nuevo_producto.save()
                  productos = Producto.objects.all()
                  return render(request, "appTerceraEntrega/productos.html", context={"productos":productos})
      else:
            formulario_producto = ProductoFormulario() # Formulario vacio para construir el html
 
      return render(request, "appTerceraEntrega/formulario/producto_formulario.html", {"formulario_producto": formulario_producto})