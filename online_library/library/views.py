from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin

from online_library.library.forms import AddBookForm, EditBookForm
from online_library.library.models import Book


class IndexView(views.ListView):
    template_name = 'base/home.html'
    model = Book


# class CreateBookView(LoginRequiredMixin, views.CreateView):
#     template_name = 'book/add-book.html'
#     model = Book
#     form_class = AddBookForm
#
#     def post(self, request, *args, **kwargs):
#         context = super().post(request, *args, **kwargs)
#         form = AddBookForm(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user_id = self.request.user.id
#             obj.save()
#         return context


def add_book(request):
    if request.method == 'GET':
        form = AddBookForm()
    else:
        form = AddBookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user_id = request.user.id
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'book/add-book.html', context=context)


class EditBook(views.UpdateView):
    template_name = 'book/edit-book.html'
    model = Book
    fields = ('title', 'description', 'image', 'type')
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
