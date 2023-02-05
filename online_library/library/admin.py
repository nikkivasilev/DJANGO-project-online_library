from django.contrib import admin

from online_library.library.models import Book


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    search_fields = ('title',)
