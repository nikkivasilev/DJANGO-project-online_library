from django.urls import path, include

from online_library.library.views import index, add_book, main_profile, edit_profile, \
    delete_profile, EditBook, DetailsBook

urlpatterns = (
    path('', index, name='index'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>', EditBook.as_view(), name='edit book'),
    path('details/<int:pk>', DetailsBook.as_view(), name='details book'),
    path('profile/', include([
        path('', main_profile, name='main profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)