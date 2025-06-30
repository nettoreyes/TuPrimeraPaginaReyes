from django import forms

class ProductoFormulario(forms.Form):
    codigo_producto = forms.CharField(max_length=13, label="Código del Producto")    
    descripcion = forms.CharField(max_length=100, label="Descripción del Producto")    
    precio = forms.IntegerField(label="Precio") 
    stock = forms.IntegerField(required=False, label="Cantidad en Stock")        
    activo = forms.BooleanField(required=False, initial=True, label="¿Producto Activo?")

class CategoriaFormulario(forms.Form):
    codigo_categoria = forms.CharField(max_length=13, label="Código ")   
    nombre_categoria = forms.CharField(max_length=100, label="Nombre de la categoria")

class ClienteFormulario(forms.Form):
    rut = forms.CharField(max_length=20, label="Rut ")   
    nombre = forms.CharField(max_length=100, label="Nombre ")  
    apellido = forms.CharField(max_length=100, label="Apellido")
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento",
        required=False,      
        widget=forms.DateInput(attrs={'type': 'date'})
    )    
    email = forms.EmailField(label="Correo Electrónico")
   
