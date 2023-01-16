from django import forms

from online_library.library.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
