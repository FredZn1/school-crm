from django.contrib import admin
from .models import Group
from students.models import Student


class StudentInline(admin.TabularInline):
    model = Student
    extra = 1
    fields = ('first_name', 'last_name', 'date_of_birth')
    classes = ('collapse',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    list_display = ('group_name', 'teacher', 'get_students_count')
    list_filter = ('teacher',)
    search_fields = ('group_name', 'teacher__first_name', 'teacher__last_name')
    ordering = ('group_name',)

    def get_students_count(self, obj):
        return obj.students.count()

    get_students_count.short_description = 'Talabalar soni'
