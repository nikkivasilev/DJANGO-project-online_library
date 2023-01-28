from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views


def index(request):
    # accounts = get_profile()
    # if not accounts:
    #     return create_profile(request)
    #
    # context = {
    #     'accounts': accounts,
    #     "books": Book.objects.all()
    # }
    #
    return render(request, 'base/home-with-profile.html')


# def create_profile(request):
#     if request.method == 'GET':
#         form = CreateProfileForm()
#     else:
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     context = {
#         'form': form,
#     }
#     return render(request, 'base/home-no-accounts.html', context=context)
#
#
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




# def details_profile(request):
#     accounts = get_profile()
#     if not accounts:
#         return create_profile(request)
#
#     context = {
#         'accounts': accounts,
#         'fullname': get_fullname(accounts)
#     }
#     return render(request, 'accounts/accounts.html', context=context)


# def edit_profile(request):
#     pass
#
#
# def delete_profile(request):
#     pass
