from django import forms

from report.models import report


class reportForm(forms.ModelForm):  
    class Meta:  
        model = report  
        fields = ['name', 'contact','fromdate','todate','trdate','fromplace','toplace','address','amount','city','passtype'] 
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'city': forms.TextInput(attrs={ 'class': 'form-control' }),
            'fromdate': forms.DateInput(attrs={ 'class': 'form-control' }),
            'todate': forms.DateInput(attrs={ 'class': 'form-control' }),
            'trdate': forms.DateInput(attrs={ 'class': 'form-control' }),
            'fromplace': forms.TextInput(attrs={ 'class': 'form-control' }),
            'toplace': forms.TextInput(attrs={ 'class': 'form-control' }),
            'address': forms.TextInput(attrs={ 'class': 'form-control' }),
             'amount': forms.TextInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
            'passtype': forms.Select(attrs={'class': 'form-control'}),  # Use Select widget here,
      }