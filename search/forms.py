# forms.py in your search app

from django import forms

class SearchForm(forms.Form):
    pass_id = forms.CharField(label='Pass ID', max_length=12)
