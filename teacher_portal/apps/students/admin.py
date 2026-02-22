from django.contrib import admin
from .models import Student, TaskCompletion


class TaskCompletionInline(admin.TabularInline):
    model = TaskCompletion
    extra = 0
    fields = ['task_number', 'completed', 'completed_at']
    readonly_fields = ['completed_at']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'group', 'completed_tasks_count', 'progress_percent', 'is_graduated', 'created_at']
    list_filter = ['group', 'group__teacher']
    search_fields = ['full_name', 'group__name']
    inlines = [TaskCompletionInline]

    def completed_tasks_count(self, obj):
        return obj.completed_tasks_count()
    completed_tasks_count.short_description = "Bajarilgan"

    def progress_percent(self, obj):
        return f"{obj.progress_percent()}%"
    progress_percent.short_description = "Foiz"

    def is_graduated(self, obj):
        return obj.is_graduated()
    is_graduated.boolean = True
    is_graduated.short_description = "Bitirgan"


@admin.register(TaskCompletion)
class TaskCompletionAdmin(admin.ModelAdmin):
    list_display = ['student', 'task_number', 'completed', 'completed_at']
    list_filter = ['completed', 'student__group']
    search_fields = ['student__full_name']
