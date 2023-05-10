from django.shortcuts import render, redirect
from .models import Volunteer, Contact, Cause,Donate

# Create your views here.
def index(request):
    causes=Cause.objects.all()
    return render(request,'index.html',{"causes":causes})

def submit_valunteer(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST.get('message')

        volunteer=Volunteer.objects.create(name=name,email=email,subject=subject,message=message)
        volunteer.save()
        return redirect('/')
    else:
        return redirect('/')

def contact(request):
    if request.method =="POST":
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        email=request.POST['email']
        message=request.POST.get('message')

        contact=Contact.objects.create(name=f"{f_name}  {l_name}",email=email,message=message)
        contact.save()
        return redirect('/')
    else:
        return redirect('/')

def donate(request,id):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        amount=request.POST.get('amount')

        cause=Cause.objects.get(id=id)
        cause.raised=cause.raised+float(amount)
        cause.goal=cause.goal-float(amount)
        cause.save()
        donation=Donate.objects.create(name=name,email=email,amount=float(amount))
        donation.save()
        return redirect('/')
    else:
        cause=Cause.objects.get(id=id)
        return render(request,'donate.html',{"cause":cause})