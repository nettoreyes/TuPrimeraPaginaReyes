from django.shortcuts import render
from .models import Post

# Create your views here.
def index( request ):
    context = { "mensaje":"Bienvenido a mi aplicación Django"}
    return render(request,"appTerceraEntrega/index.html", context)

def post_list( request ):
    post_list = Post.objects.all()
    return render(request, "appTerceraEntrega/post_list.html", context={"posts":post_list})