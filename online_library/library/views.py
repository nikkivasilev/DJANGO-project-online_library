from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from online_library.library.forms import CreateProfileForm, AddBookForm
from online_library.library.models import Profile, Book


# Create your views here.
def get_profile():
    try:
        return Profile.objects.all().get()
    except Profile.DoesNotExist:
        return None

def get_fullname(profile):
    firstname = profile.first_name if profile.first_name else ''
    lastname = profile.last_name if profile.last_name else ''
    fullname = [firstname, lastname]
    return ' '.join(fullname).strip()

def index(request):
    profile = get_profile()
    if not profile:
        return create_profile(request)

    context = {
        'profile': profile,
        "books": Book.objects.all()
    }

    return render(request, 'base/home-with-profile.html', context=context)


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
    return render(request, 'base/home-no-profile.html', context=context)


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


class EditBook(views.UpdateView):
    template_name = 'book/edit-book.html'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('index')


def delete_book(request, pk):
    book = Book.objects \
        .filter(id=pk)
    if book:
        book.delete()
    return redirect('index')


class DetailsBook(views.DetailView):
    template_name = 'book/book-details.html'
    model = Book

# class DetailsProfile(views.DetailView):
#     template_name = 'profile/profile.html'
#     model = Profile


def details_profile(request):
    profile = get_profile()
    if not profile:
        return create_profile(request)

    context = {
        'profile': profile,
        'fullname': get_fullname(profile)
    }
    return render(request, 'profile/profile.html', context=context)

def edit_profile(request):
    pass


def delete_profile(request):
    pass
