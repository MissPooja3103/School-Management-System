from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from studentapp.models import Student # type: ignore
from django.contrib import messages


# Create your views here.


def home_view(request):
    return render(request,'studentapp/home.html')



def register_view(request):
    if request.method == 'POST':
        print(request.POST)
        un = request.POST.get('uname')
        em = request.POST.get('email')
        pwd = request.POST.get('pwd')

        if User.objects.filter(username=un).exists():
            print("User Already Exists")
            return render(request,"studentapp/register.html",{'error':"User Already Exists"})
        
        else:
            user = User.objects.create_user(username=un, email=em, password=pwd)
            print("User Created Successfully!")
            return redirect('login')
        
    return render(request,'studentapp/register.html')


def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        un = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        user = authenticate(username=un, password=pwd)
        if user is not None:
            login(request, user)
            print("User is now Logged in!")
            print("Authentication Successful!")
            return redirect('home')
        else:
            return render(request,'login.html',{'error' : "Invalid Username or Password"})

    return render(request,'studentapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def create_view(request):
    if request.method == 'POST':
         print(request.POST)
         r = request.POST.get("roll")
         n = request.POST.get("nm")
         m = request.POST.get("marks")
         print(f"Student Name is {n} and Marks is {m}")
         obj = Student(roll = r, name = n, marks = m)
         obj.save()
         print("Student's Data Saved Successfully!")
         return redirect("/studentapp/display/")


    return render(request,'studentapp/create.html')


def display_view(request):
    data = Student.objects.all()
    context={"data": data}
    return render(request,'studentapp/display.html',context)


def delete_view(request, id):
    print("In delete View", id)
    obj= Student.objects.get(pk=id)
    obj.delete()
    return redirect('display')

def update_view(request, id):
    print("In Update View", id)
    obj = Student.objects.get(pk=id)

    if request.method == 'POST':
        r = request.POST.get("roll")
        n = request.POST.get("nm")
        m = request.POST.get("marks")
        
        # Update the object with the new values
        obj.roll = r
        obj.name = n
        obj.marks = m
        
        # Save the updated object to the database
        obj.save()
        
        # Redirect to the 'display' page after saving the changes
        return redirect('display')

    # Render the update template with the existing object data
    return render(request, "studentapp/update.html", {'obj': obj})

