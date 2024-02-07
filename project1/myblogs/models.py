from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.
class Blog_Category(models.Model):
    blog_cat = models.CharField(max_length=60,unique=True)
    blogcat_img = models.ImageField(upload_to='images/')
    blogcat_description= RichTextField()
    def __str__(self):
        return self.blog_cat
    
class subscription(models.Model):
    email = models.EmailField(unique=True)
    def _str_(self):
        return self.email


class blog_Post(models.Model):
    blog_name =models.CharField(max_length=100)
    cover_img=models.ImageField(upload_to='images/')
    blog_description=RichTextField()
    blog_cat=models.ForeignKey(Blog_Category ,on_delete=models.CASCADE)
    def __str__(self):
        return self.blog_name