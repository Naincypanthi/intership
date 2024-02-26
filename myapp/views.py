from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import web 
from .models import user
from django.db import connection
def amount(request):
    if(request.method=="POST"):
        categories=request.POST['categories']
        date=request.POST['date']
        amount=request.POST['amount']
        mycur=connection.cursor()
        mycur.execute("insert into myapp_web (categories,date,amount) values (%s,%s,%s)",[categories,date,amount])
        ob=web.objects.all()
        data={
            "emp":ob
        }
        return render(request,"temp.html",data)
    else:
        return render(request,"temp.html")
# def display(request):
#     mycur=connection.cursor()
#     mycur.execute("select * from myapp_web")
#     ob=mycur.fetchall()
#     data={
#         "emp":ob
    # }
    # return render(request,"temp.html",data)
def registration(request):
    return render(request,"registration.html")
def login(request):
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['password']
        data=user.objects.filter(email=email,password=password).exists()
        if(data):
            request.session['user']="admin"
            return redirect(dashboard)
        else:
            return redirect(invalid)
    else:
        return render(request,"login.html")
def dashboard(request):
    if "user" in request.session:
        return HttpResponse("welcome user")
    else:
        return redirect(invalid)
def invalid(request):
    return HttpResponse("invalid")
def logout(request):
    request.session.pop("user")
    return redirect(login)
    



# Create your views here.
