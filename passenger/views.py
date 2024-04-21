from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from passenger.forms import passengerForm  
from passenger.models import passenger

# Create your views here.
def addnew(request):  
    if request.method == "POST":  
        form = passengerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('passenger:index')  
            except:  
                pass
    else:  
        form = passengerForm()  
    return render(request,'passenger/index.html',{'form':form})  
 
def index(request):  
    passengers = passenger.objects.all()  
    return render(request,"passenger/show.html",{'passenger':passengers})  
 
def edit(request, id):  
    passengers = passenger.objects.get(id=id)  
    return render(request,'passenger/edit.html', {'passenger':passengers})  
 
def update(request, id):  
    passengers = passenger.objects.get(id=id)  
    form = passengerForm(request.POST, instance = passengers)  
    if form.is_valid():  
        form.save()  
        return redirect('/')  
    return render(request, 'passenger/edit.html', {'passenger': passengers})  
     
def destroy(request, id):  
    passengers = passenger.objects.get(id=id)  
    passengers.delete()  
    return redirect('/')  