import base64
from django.shortcuts import render
import qrcode
from io import BytesIO
from .forms import SearchForm
from transaction.models import transaction  # Assuming Transaction is the correct model name

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            pass_id = form.cleaned_data['pass_id']
            transaction_instance = transaction.objects.filter(id=pass_id).first()  # Using 'transaction_instance' to avoid naming conflict
            if transaction_instance:
                # Generate QR code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=6,
                    border=4,
                )
                qr.add_data(str(transaction_instance))
                qr.make(fit=True)
                qr_img = qr.make_image(fill_color="black", back_color="white")
                # Convert QR code image to base64
                buffer = BytesIO()
                qr_img.save(buffer, format='PNG')
                qr_img_base64 = base64.b64encode(buffer.getvalue()).decode()
                return render(request, 'search/results.html', {'transaction': transaction_instance, 'qr_code_image_base64': qr_img_base64})
            else:
                return render(request, 'search/no_results.html')
    else:
        form = SearchForm()    
    return render(request, 'search/search.html', {'form': form})
