from django.shortcuts import render
import barcode
from barcode.writer import ImageWriter

def generate_barcode(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        if code:
            # Generate barcode
            ean = barcode.get('ean13', code, writer=ImageWriter())
            filename = ean.save('barcode')
            barcode_filepath = f'/media/{filename}'
            return render(request, 'barcode_generator/barcode.html', {'barcode_filepath': barcode_filepath})
    return render(request, 'qrcode/generate_barcode.html')

