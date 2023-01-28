
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('online_library.library.urls')),
    path('accounts/', include('online_library.accounts.urls')),

]
