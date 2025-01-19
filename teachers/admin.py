from django.contrib import admin
from django.utils.html import format_html
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'subject', 'email', 'work_experience', 'show_image')
    list_filter = ('subject', 'work_experience')
    search_fields = ('first_name', 'last_name', 'email', 'telephone_number')
    ordering = ('first_name', 'last_name')

    fieldsets = (
        ('Personal Information', {
            'fields': (
                ('first_name', 'last_name'),
                'image'
            )
        }),
        ('Professional Information', {
            'fields': (
                'subject',
                'work_experience',
                'email'
            )
        }),
        ('Contact Information', {
            'fields': ('telephone_number',)
        })
    )

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    get_full_name.short_description = 'Full Name'

    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.image.url)
        return "No Image"

    show_image.short_description = 'Photo'
