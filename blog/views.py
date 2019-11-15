from django.shortcuts import render, HttpResponse
from blog.models import Category, Post, Comment

# Create your views here.
def blog(request):
    categorys = Category.objects.all()
    return render(request, "blog/index.html", {"categorys": categorys})

def post(request):
    return HttpResponse("<h1>Post</h1>")