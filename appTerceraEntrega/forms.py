from django import forms

class ProductoFormulario(forms.Form):
    codigo_producto = forms.CharField(max_length=13, label="Código del Producto") # Este seguirá siendo obligatorio    
    descripcion = forms.CharField(max_length=100, label="Descripción del Producto")    
    precio = forms.IntegerField(label="Precio") # Este seguirá siendo obligatorio    
    stock = forms.IntegerField(required=False, label="Cantidad en Stock")        
    activo = forms.BooleanField(required=False, initial=True, label="¿Producto Activo?")