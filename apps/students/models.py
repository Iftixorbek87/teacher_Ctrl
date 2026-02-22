from django.db import models
from apps.groups.models import Group


class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students', verbose_name="Guruh")
    full_name = models.CharField(max_length=200, verbose_name="To'liq ismi")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

    def completed_tasks_count(self):
        return self.task_completions.filter(completed=True).count()

    def progress_percent(self):
        total = self.group.total_tasks
        if total == 0:
            return 0
        return round((self.completed_tasks_count() / total) * 100)

    def is_graduated(self):
        return self.completed_tasks_count() >= self.group.total_tasks


class TaskCompletion(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='task_completions')
    task_number = models.IntegerField(verbose_name="Vazifa raqami")
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ['student', 'task_number']
        verbose_name = "Vazifa bajarishi"
        verbose_name_plural = "Vazifa bajarishlari"

    def __str__(self):
        return f"{self.student.full_name} - Vazifa {self.task_number}"
