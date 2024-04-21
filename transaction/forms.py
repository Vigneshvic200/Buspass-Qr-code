from django import forms
from transaction.models import transaction

class transactionForm(forms.ModelForm):  
    class Meta:  
        model = transaction  
        fields = ['name', 'contact','fromdate','todate','trdate','fromplace','toplace','address','amount','city','passtype'] 
        widgets = { 
            'name': forms.TextInput(attrs={'class': 'form-control'}), 
            'city': forms.TextInput(attrs={'class': 'form-control'}),
           'fromdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'todate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fromplace': forms.TextInput(attrs={'class': 'form-control'}),
            'toplace': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'passtype': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.error_messages = {'required': f"{field.label} is required."}
