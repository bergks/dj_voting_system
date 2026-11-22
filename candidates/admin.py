from django.contrib import admin
from .models import Candidate, Category


class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'director',
        'year',
        'description',
    )
    list_editable = (
        'description',
    )
    search_fields = ('title',)
    list_filter = ('category',)
    filter_horizontal = ('category',)


@admin.register(Category)
class CategoryRegister(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug'
    )
    list_editable = (
        'title',
        'slug',
    )
    list_display_links = ('id', )
    search_fields = ('title',)


admin.site.register(Candidate, CandidateAdmin)
