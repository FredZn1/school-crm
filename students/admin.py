from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'group', 'date_of_birth', 'telephone_number')
    list_filter = ('group', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'telephone_number', 'group__name')
    ordering = ('last_name', 'first_name')
    fieldsets = (
        (None, {
            'fields': ('image', 'first_name', 'last_name', 'group', 'date_of_birth')
        }),
        ('Contact Information', {
            'fields': ('telephone_number', 'address')
        }),
    )
