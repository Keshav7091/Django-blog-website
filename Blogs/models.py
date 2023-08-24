
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html
# Create your models here.

class ContactUsTb(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=90)
    phone=models.IntegerField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name


class Popular_Blogs(models.Model):
    title= models.CharField(max_length=122)
    author =models.CharField(max_length=90)
    posted_date= models.DateField(auto_now_add=True)
    content= RichTextField()
    # url = models.CharField(max_length=100)
    create_at= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title



class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=122)
    posted_date= models.DateField(auto_now_add=True)
    content= RichTextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    create_at= models.DateTimeField(auto_now_add=True, null=True)


    def image_tag(self):
        return format_html("<img src='/media/{}' style='width:40px; height:40px; border-radius: 50%;' />".format(self.image))

    def __str__(self) -> str:
        return self.title

class Regular_Blog(models.Model):
    Blog_id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=122)
    author =models.CharField(max_length=90)
    posted_date= models.DateField(auto_now_add=True)
    content= RichTextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Regular_Blog/')
    create_at= models.DateTimeField(auto_now_add=True)


    def image_tag(self):
        return format_html("<img src='/media/{}' style='width:40px; height:40px; border-radius: 50%;' />".format(self.image))

    def __str__(self) -> str:
        return self.title