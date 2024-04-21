from django import forms

from passes.models import Passes 


class passesForm(forms.ModelForm):  
    class Meta:  
        model = Passes  
        fields = ['name','passtype','city','amount'] 
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'city': forms.TextInput(attrs={ 'class': 'form-control' }),
            'passtype': forms.Select(attrs={'class': 'form-control'}), 
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            
          
      }