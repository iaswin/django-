from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    
    return render(request,"app/index.html")

def about(request):
    
    return render(request,"app/about.html")

def booking(request):
    
    return render(request,"app/booking.html")

def contact(request):
    
    return render(request,"app/contact.html")

def html(request):
    return render(request,"app/forms.html")

def insertdata(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['emmail']
    
    
    newuser=Teacher.objects.create(FirstName=fname,LastName=lname,Email=email) 
     
    return redirect('show')
def showpage(request):
    all_data=Teacher.objects.all()
    return render(request,"app/show.html",{'key1':all_data})


def editpage(request,pk):
    getdata=Teacher.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':getdata})

def updatepage(request,pk):
    udata=Teacher.objects.get(id=pk)
    udata.FirstName=request.POST['fname']
    udata.LastName=request.POST['lname']
    udata.Email=request.POST['emmail']
    
    udata.save()
    return redirect('show')

def deletedata(request,pk):
    ddata=Teacher.objects.get(id=pk)
    ddata.delete()
    return redirect('show')

def registerpage(request):
    return render(request,"app/register.html")

def User(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
    
    #validate for already exist
        user=Users.objects.filter(Email=email)
        if user:
            message="user already exist"
            return render(request,"app/login.html",{'msg':message})
        else:
            if password==cpassword:
                newuser=Users.objects.create(FirstName=fname,LastName=lname,Email=email,Password=password)
                message="user registered"
                return render(request,"app/login.html",{'msg':message})
            else:
                message="check your password"
                return render(request,"app/register.html",{'msg':message})



def Login(request):
    return render(request,"app/login.html")


def loguser(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=Users.objects.get(Email=email)
        
        if user:
            if user.Password==password:
                request.session['FirstName']=user.FirstName
                return render(request,"app/home.html")
            else:
                message="check your password"
                return render(request,"app/login.html",{'msg':message})
            
        else:
                message="user doesnt exit"
                return render(request,"app/register.html",{'msg':message})
            
def image(request):
    return render(request,"app/image.html")

def upload(request):
    if request.method=="POST":
        imgfile=request.FILES['imgg']
        new=imagges.objects.create(image=imgfile)
        return render(request,"app/show1.html")
    