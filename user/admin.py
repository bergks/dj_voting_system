from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'name',
        'surname'
    )

    search_fileds = ('username',)

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(User, UserAdmin)
