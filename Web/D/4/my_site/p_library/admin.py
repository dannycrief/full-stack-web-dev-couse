from django.contrib import admin
from .models import Redaction, Book, Author, Inspiration


class AuthorsInlineAdmin(admin.TabularInline):
    model = Book.authors.through


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.authors

    list_display = (
        'title',
        'author_full_name',
    )
    fields = (
        'ISBN',
        'title',
        'description',
        'year_release',
        'price',
        'copy_count',
        'redaction',
    )
    inlines = (AuthorsInlineAdmin,)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Inspiration)
class InspirationAdmin(admin.ModelAdmin):
    pass


@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
    pass
