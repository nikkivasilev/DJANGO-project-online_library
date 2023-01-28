from django.urls import path

from online_library.library.views import index, add_book, EditBook, DetailsBook, delete_book

urlpatterns = (
    path('', index, name='index'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>', EditBook.as_view(), name='edit book'),
    path('delete/<int:pk>', delete_book, name='delete book'),
    path('details/<int:pk>', DetailsBook.as_view(), name='details book'),
)