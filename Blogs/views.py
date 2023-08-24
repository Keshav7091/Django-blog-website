from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def home(request):

    popularBlogs= Popular_Blogs.objects.all()
    context = {'poplarBLOGS':popularBlogs,'name':'Mr. Ram'}


    return render(request , 'home.html',context)


def view_blog(request,pk):
    viewBlog = Popular_Blogs.objects.get(pk=pk)

    return render(request,'viewBlog.html', {'viewBlog': viewBlog})
    
    
def about(request):
    return render(request , 'about.html')


def contact(request):

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

    return render(request , 'contact.html')

def write(request):
    if request.method == 'POST':
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        cat_id = request.POST['cat']
        category = Category.objects.get(id=cat_id)
        new_blog = Regular_Blog(author_name=author, title=title, content=content, catagory=category)
        new_blog.save()
    cat = Category.objects.all()
    return render(request, 'write.html', {'cat':cat})
