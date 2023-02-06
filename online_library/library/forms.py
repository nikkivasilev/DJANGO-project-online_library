from django import forms

from online_library.library.models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('user',)


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('user',)
