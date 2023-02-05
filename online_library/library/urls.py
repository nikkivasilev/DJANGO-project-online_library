from django.urls import path

from online_library.library.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('add/', add_book, name='add book'),
    # path('edit/<int:pk>', EditBook.as_view(), name='edit book'),
    # path('delete/<int:pk>', delete_book, name='delete book'),
    # path('details/<int:pk>', DetailsBook.as_view(), name='details book'),
]
