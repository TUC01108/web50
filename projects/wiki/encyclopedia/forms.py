from django import forms

class SearchForm(forms.Form):
    your_search = forms.CharField(max_length=100)