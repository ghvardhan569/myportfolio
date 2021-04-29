from django.shortcuts import render, HttpResponse
from home.models import Connect2me

# Create your views here.
def home(request):
    #return HttpResponse("This is a Home Page")
    #context={'name':'Harsha Vardhan Garlapati','course':'Django'}
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("This is a About Page")
    return render(request, 'about.html')

def certificates(request):
    #return HttpResponse("This is a About Page")
    return render(request, 'certificates.html')

def projects(request):
    #return HttpResponse("This is a Projects Page")
    return render(request, 'projects.html')

def connect2me(request):
    if request.method=="POST":
        #print("This is post method")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        #print(name, email, phone, desc)
        ins = Connect2me(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("the data is written is to db")

    #return HttpResponse("This is a Contact Page")
    return render(request, 'connect2me.html')