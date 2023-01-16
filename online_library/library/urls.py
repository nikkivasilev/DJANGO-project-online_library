from django.urls import path, include

from online_library.library.views import index, add_book, edit_book, details_book, main_profile, edit_profile, \
    delete_profile

urlpatterns = (
    path('', index, name='index'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('details/<int:pk>', details_book, name='details book'),
    path('profile/', include([
        path('', main_profile, name='main profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)