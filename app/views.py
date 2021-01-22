from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Navbar
from .models import Contact
from .models import Blog
from django.views.generic import ListView
def index(request):
    navbar = Navbar.objects.all()
    cont = Contact.objects.all()
    Blog_Element = Blog.objects.all()
    return render(request,'index.html',{'navbar':navbar,'cont':cont,'Blog_Element':Blog_Element})


def blog_list(request,pk):
    navbar = Navbar.objects.all()
    each_post = Blog.objects.get(pk=pk)
    context = {
        'object_list':each_post,
        'navbar':navbar
    }
    return render(request,'index/blog.html',context)

