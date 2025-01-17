from django.contrib import admin
from django.utils.html import format_html
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'group', 'date_of_birth', 'telephone_number', 'show_image')
    list_filter = ('group', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'group__group_name', 'telephone_number', 'address')
    ordering = ('last_name', 'first_name')

    fieldsets = (
        ('Personal Information', {
            'fields': ('image', 'first_name', 'last_name', 'date_of_birth')
        }),
        ('Group Information', {
            'fields': ('group',)
        }),
        ('Contact Information', {
            'fields': ('telephone_number', 'address')
        }),
    )

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = 'Full Name'

    def show_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;" alt="Student Image"/>',
                obj.image.url
            )
        return "No Image"

    show_image.short_description = 'Photo'
