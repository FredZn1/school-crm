from django.contrib import admin
from django.utils.html import format_html
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'email', 'work_experience', 'display_image')
    list_filter = ('subject', 'work_experience')
    search_fields = ('first_name', 'last_name', 'email', 'telephone_number')
    ordering = ('first_name', 'last_name')

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'telephone_number', 'email', 'image')
        }),
        ('Professional Information', {
            'fields': ('subject', 'work_experience')
        }),
    )

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = 'Full Name'

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50%;" />',
                obj.image.url
            )
        return "No Image"

    display_image.short_description = 'Photo'
