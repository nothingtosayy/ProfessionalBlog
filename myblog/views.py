from django.shortcuts import render
from myblog.models import *
# Create your views here.
def home(request):
    return render(request, 'blog.html')

def blog(request):
    articles = Post.objects.all()
    return render(request, 'writeblog.html', {'articles': articles})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']
        k = Contact(name=name, email=email, query=query)
        k.save()

    return render(request, 'contactus.html')

def about(request):
    return render(request, 'aboutus.html')