from django.contrib import admin
from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'get_student_count', 'total_tasks', 'created_at']
    list_filter = ['teacher', 'created_at']
    search_fields = ['name', 'teacher__username']
    readonly_fields = ['created_at']

    def get_student_count(self, obj):
        return obj.get_student_count()
    get_student_count.short_description = "O'quvchilar soni"
