from django.shortcuts import render
from .models import Post, Producto, Categoria, Cliente
from .forms import ProductoFormulario, CategoriaFormulario, ClienteFormulario
from django.http import HttpResponse

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

def categorias( request ):  
    categorias = Categoria.objects.all()  
    return render(request, "appTerceraEntrega/categorias.html", context={"categorias":categorias})

def clientes( request ):  
    clientes = Cliente.objects.all()  
    return render(request, "appTerceraEntrega/clientes.html", context={"clientes":clientes})

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

def categoria_formulario(request):
      if request.method == "POST":
            formulario_categoria = CategoriaFormulario(request.POST) 
            if formulario_categoria.is_valid():
                  datos = formulario_categoria.cleaned_data   

                  nueva_categoria = Categoria(codigo_categoria=datos["codigo_categoria"],nombre_categoria=datos["nombre_categoria"])
                  nueva_categoria.save()
                  categorias = Categoria.objects.all()
                  return render(request, "appTerceraEntrega/categorias.html", context={"categorias":categorias})
      else:
            formulario_categoria = CategoriaFormulario()
 
      return render(request, "appTerceraEntrega/formulario/categoria_formulario.html", {"formulario_categoria": formulario_categoria})

def cliente_formulario(request):
      if request.method == "POST":
            formulario_cliente = ClienteFormulario(request.POST) 
            if formulario_cliente.is_valid():
                  datos = formulario_cliente.cleaned_data   

                  nuevo_cliente = Cliente(rut=datos["rut"],nombre=datos["nombre"],apellido=datos["apellido"],fecha_nacimiento=datos["fecha_nacimiento"],email=datos["email"])
                  nuevo_cliente.save()
                  clientes = Cliente.objects.all()
                  return render(request, "appTerceraEntrega/clientes.html", context={"clientes":clientes})
      else:
            formulario_cliente = ClienteFormulario()
 
      return render(request, "appTerceraEntrega/formulario/cliente_formulario.html", {"formulario_cliente": formulario_cliente})

def busquedaProducto(request):
    return render(request, "appTerceraEntrega/formulario/busquedaProducto.html")


def buscar(request):
    if request.GET["codigo_producto"]:        
        codigo_producto = request.GET['codigo_producto']
        # icontains es un filtro que se usa para buscar coincidencias en los campos de texto de la base de datos, 
        # sin importar si las letras están en mayúsculas o minúsculas
        productos = Producto.objects.filter(codigo_producto__icontains=codigo_producto)

        return render(request, "appTerceraEntrega/formulario/resultadosBusqueda.html", {"productos": productos, "codigo_producto": codigo_producto})

    else:
        respuesta = "No enviaste datos"

        # No olvidar from django.http import HttpResponse
        return HttpResponse(respuesta)