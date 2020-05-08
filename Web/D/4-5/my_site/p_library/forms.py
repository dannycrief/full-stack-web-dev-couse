from django import forms
from .models import Authors, Book


class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Authors
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
