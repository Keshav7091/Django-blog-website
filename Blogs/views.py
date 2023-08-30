from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def home(request):

    popularBlogs= Popular_Blogs.objects.all()
    cats = Category.objects.all()
    context = {'poplarBLOGS':popularBlogs,'name':'Mr. Ram', 'cats': cats}


    return render(request , 'home.html',context)


def view_blog(request,pk):
    viewBlog = Popular_Blogs.objects.get(pk=pk)
    cats = Category.objects.all()

    return render(request,'viewBlog.html', {'viewBlog': viewBlog, 'cats': cats})
    
    
def about(request):
    
    cats = Category.objects.all()
    return render(request , 'about.html', {'cats': cats})


def contact(request):

    cats = Category.objects.all()
    if request.method == 'POST':
        cname = request.POST['fullname']
        cemail = request.POST['email']
        cphonenumber = request.POST['phone']
        cmsg = request.POST['message']

        if len(cname)>1 and len(cemail)>15 and len(cphonenumber)==10 and len(cmsg)>20:

        
            contactObj = ContactUsTb(name=cname , email=cemail, phone=cphonenumber, message = cmsg)
            contactObj.save()

        else:
            return HttpResponse("fill invalid form")

    return render(request , 'contact.html', {'cats': cats})


def AllBlog(request):

    regularBlogs= Regular_Blog.objects.all()
    cats = Category.objects.all()

    context = {'regularBLOGS':regularBlogs, 'cats': cats}


    return render(request , 'blog.html',context)

def all_blogs(request,pk):
    allBlogs = Regular_Blog.objects.get(pk=pk)
    cats = Category.objects.all()

    return render(request,'viewAllBlogs.html', {'allBlogs': allBlogs, 'cats': cats})


def category(request, pk):
    cats = Category.objects.all()
    cat = Category.objects.get(pk=pk)
    posts = Regular_Blog.objects.filter(cat=cat)

    return render(request, 'category.html', {'cat':cat, 'posts':posts, 'cats': cats})


def search(request):
    return render(request, 'search.html')