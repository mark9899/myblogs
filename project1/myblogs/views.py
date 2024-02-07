from itertools import product
from django.shortcuts import render 
from django.http import HttpResponse
from .form import Blog_Form
from django.shortcuts import redirect
from .models import Blog_Category, blog_Post ,subscription
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate ,login ,logout 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
# from django.shortcuts import get_object_or_404




# Create your views here.
def home(request):
    y=Blog_Category.objects.all()
    return render(request , "myblogs/home.html" ,{"category":y})

def findproduct(request):
    if request.method == 'POST':
        x = request.POST.get('prod_search')
        #print(x)
        mydata = blog_Post.objects.filter(Q(blog_cat__blog_cat__icontains = x) |Q(blog_name__icontains = x) )
        #print(mydata)
        if mydata:
             return render(request , "myblogs/home.html" ,{"category":mydata}) 
        else:
            return render(request , "myblogs/home.html" ,{"warning":'No Record Found'}) 
def support(request):
    return render(request , "myblogs/support.html" )


# def blog(request):
#     x= Blog_Form()  
#     if request.method == "GET":
#         return render(request,'myblogs/blog.html',{"x":x})
#     else:
#         print("hi")
#         form = Blog_Form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             print("hi")
#             return redirect('home')
#         else:
#             return render(request,'myblogs/blog.html',{"x":x})

def newsletter(request):
#    return HttpResponse('<h1> Sucbcribe to Our Newsletter </h1>')
   if request.method == 'GET':
        return render(request, 'myblogs/newsletter.html')
   elif request.method == 'POST':
        email = request.POST.get('email')
        y = subscription(email=email)
        if(subscription.objects.filter(email = email).exists()):
          return render(request,"myblogs/newsletter.html",{'feedback':'You are already subscribed'})   
        else:
          y.save()
          print(email)
          return render(request,"myblogs/newsletter.html",{'feedback':'You are subscribed now'})

def ck(request):
    x=Blog_Form()
    return render(request,'myblogs/ck.html',{"x":x})
   


def allblogs(request):
    y=blog_Post.objects.all()
    paginator = Paginator(y, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'myblogs/allblogs.html',{"y":page_obj})

    #return render(request,'myblogs/allblogs.html',{"y":y})


    

@login_required(login_url="loginuser")
def blog_details(request, blog_id):
    y=blog_Post.objects.get(id=blog_id)
    return render(request,'myblogs/blog_details.html',{"y":y})

def loginuser(request):
     if request.method == 'GET' :
        return render (request,'myblogs/loginuser.html',{'form': AuthenticationForm()})
     else:
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(request, username=a, password=b)
        if user is None:
            return render(request,'myblogs/loginuser.html',{'from':AuthenticationForm(),'error':'Invalid credential'})
        else:
             login(request, user)
             return redirect('home')
        
def signuser(request):
     if request.method == 'POST':
        return render (request,'myblogs/signuser.html',{'form': UserCreationForm()})
     else:
        a = request.POST.get( 'username' )
        b = request.POST.get( 'password1')
        c = request.POST.get( 'password2')
        if b==c:
             if(User. objects.filter(username = a)):
                 return render(request, 'myblogs/signuser.html',{'form': UserCreationForm(), 'error':'User name already exits TY' })
             else:
                 user =User.objects.create_user(username = a, password = b)
                 user.save()
                 login(request,user)
                 return redirect('home')
        else:
             return render(request, 'myblogs/signuser.html',{'form': UserCreationForm(),'error':'Password Mismatch Try Again' })
def logoutuser(request):
     if request.method == 'GET' :
        logout(request)
        return redirect('home')
     
def blog(request):
    # Extract the category from the request parameters
    category_name = request.GET.get('category')

    # If a category is provided, filter blog posts by that category, otherwise, get all blog posts
    if category_name:
        blogs = blog_Post.objects.filter(blog_cat__blog_cat=category_name)
    else:
        blogs = blog_Post.objects.all()

    return render(request, 'myblogs/allblogs.html', {"blogs": blogs, "category": category_name})

def cat(request, cat_id):
    x = Blog_Category.objects.get(blog_cat = cat_id)
    blogs = blog_Post.objects.filter(blog_cat=x)
    return render(request,'myblogs/allblogs.html',{"y":blogs})
