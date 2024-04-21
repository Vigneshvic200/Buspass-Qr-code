from django import forms
from django.core.exceptions import ValidationError
from passenger.models import passenger

class passengerForm(forms.ModelForm):
    class Meta:
        model = passenger
        fields = ['name', 'contact', 'city']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise ValidationError("Name must be at least 2 characters long.")
        return name

    def clean_contact(self):
        contact = self.cleaned_data['contact']
        if not contact.isdigit():
            raise ValidationError("Contact must contain only digits.")
        return contact

    def clean_city(self):
        city = self.cleaned_data['city']
        # Add your validation logic for city field
        return city
 