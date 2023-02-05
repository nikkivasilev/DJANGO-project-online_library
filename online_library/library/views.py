from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from online_library.library.models import Book


class IndexView(views.ListView):
    template_name = 'base/home.html'
    model = Book



# def add_book(request):
#     if request.method == 'GET':
#         form = AddBookForm()
#     else:
#         form = AddBookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'book/add-book.html', context=context)
#
#
# class EditBook(views.UpdateView):
#     template_name = 'book/edit-book.html'
#     model = Book
#     fields = '__all__'
#     success_url = reverse_lazy('index')
#
#
# def delete_book(request, pk):
#     book = Book.objects \
#         .filter(id=pk)
#     if book:
#         book.delete()
#     return redirect('index')
#
#
# class DetailsBook(views.DetailView):
#     template_name = 'book/book-details.html'
#     model = Book
