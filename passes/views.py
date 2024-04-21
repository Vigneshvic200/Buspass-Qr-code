from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from passes.forms import passesForm  
from passes.models import Passes

# Create your views here.
def addnew(request):  
    if request.method == "POST":  
        form = passesForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('passes:index')  
            except:  
                pass
    else:  
        form = passesForm()  
    return render(request,'passes/index.html',{'form':form})  
 
def index(request):  
    passes = Passes.objects.all()  
    return render(request,"passes/show.html",{'passes':passes})  
 
def edit(request, id):  
    passes = Passes.objects.get(id=id)  
    return render(request,'passes/edit.html', {'passes':passes})  
 
def update(request, id):  
    passes = Passes.objects.get(id=id)  
    form = passesForm(request.POST, instance = passes)  
    if form.is_valid():  
        form.save()  
        return redirect('/')  
    return render(request, 'passes/edit.html', {'passes': passes})  
     
def destroy(request, id):  
    passes = Passes.objects.get(id=id)  
    passes.delete()  
    return redirect('/')  