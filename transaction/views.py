import base64
from datetime import date
import io
import os
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

# Create your views here.
from django.shortcuts import redirect, render
import qrcode
from barcode.writer import ImageWriter
from bus import settings
from transaction.forms import transactionForm  
from transaction.models import transaction
from passenger.models import passenger

# Create your views here.
def addnew(request):  
    if request.method == "POST":  
        form = transactionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('transaction:index')  
            except:  
                pass
    else:  
        form = transactionForm()  
    return render(request,'transaction/index.html',{'form':form})  
 
def index(request):  
    transactions = transaction.objects.all()  
    return render(request,"transaction/show.html",{'transaction':transactions})  
 
def edit(request, id):  
    transactions = transaction.objects.get(id=id)  
    return render(request,'transaction/edit.html', {'transaction':transactions})  
 
def update(request, id):  
    transactions = transaction.objects.get(id=id)  
    form = transactionForm(request.POST, instance = transactions)  
    if form.is_valid():  
        form.save()  
        return redirect('/')  
    return render(request, 'transaction/edit.html', {'transaction': transactions})  
     
def destroy(request, id):  
    transactions= transaction.objects.get(id=id)  
    transactions.delete()  
    return redirect('/')  
def bill_print(request, id):
    transaction_instance = get_object_or_404(transaction, id=id)
    number = str(id).zfill(12)  # Ensure the ID is 12 digits long
    
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(number)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Prepare BytesIO object to store image bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    # Encode image bytes as Base64 string
    img_base64 = base64.b64encode(img_byte_arr.read()).decode('utf-8')
    
    # Prepare context for template
    context = {
        'transaction': transaction_instance,
        'qr_code_image_base64': img_base64
    }
    
    # Render HTML template
    return render(request, 'transaction/bill_print.html', context)
def get_passenger_details(request):
    if request.method == 'GET' and 'name' in request.GET:
        name = request.GET.get('name')
        try:
            passenger = passenger.objects.get(name=name)
            data = {
                'city': passenger.city,
                'contact': passenger.contact
            }
            return JsonResponse(data)
        except passenger.DoesNotExist:
            return JsonResponse({'error': 'Passenger not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def my_view(request):
    # Your view logic here
    
    context = {
        # Other context variables
        'today': date.today()
    }


    def get_passenger_data(request):
        name = request.GET.get('name')
    try:
        passengers = Passenger.objects.get(name=name)
        passenger_data = {
            'name': passenger.name,
            'city': passenger.city,
            'contact': passenger.contact
        }
        return JsonResponse({'passenger': passenger_data})
    except passengerForm.DoesNotExist:
        return JsonResponse({'error': 'Passenger not found'}, status=404)