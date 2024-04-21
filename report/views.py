# report/views.py

from django.shortcuts import render
from transaction.models import transaction

def report_view(request):
    transactions = transaction.objects.all()
    return render(request, 'report/index.html', {'transactions': transactions})
