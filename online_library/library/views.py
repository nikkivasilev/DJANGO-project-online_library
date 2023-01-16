from django.shortcuts import render, redirect

from online_library.library.forms import CreateProfileForm, AddBookForm
from online_library.library.models import Profile, Book


# Create your views here.
def get_profile():
    try:
        return Profile.objects.all().get()
    except Profile.DoesNotExist:
        return None

def index(request):
    profile = get_profile()
    if not profile:
        return create_profile(request)

    context = {
        'profile': profile,
        "books": Book.objects.all()
    }

    return render(request, 'profile/home-with-profile.html', context=context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'profile/home-no-profile.html', context=context)

def add_book(request):
    if request.method == 'GET':
        form = AddBookForm()
    else:
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'book/add-book.html', context=context)


def edit_book(request, pk):
    pass

def details_book(request, pk):
    pass

def main_profile(request):
    pass

def edit_profile(request):
    pass

def delete_profile(request):
    pass
