import email
import imp
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context= { "variable":"this is sent"
        
    }
    
    return render(request,"index.html",context)

    
    

def about(request):
    return render(request,"about.html")
    
    #return HttpResponse("THIS IS about PAGE")

def services(request):
    return render(request,"services.html")
    
    #return HttpResponse("THIS IS service PAGE")

def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message Has Been Delivered.')
    
    return render(request,"contact.html")
    
    #return HttpResponse("THIS IS contact PAGE")




