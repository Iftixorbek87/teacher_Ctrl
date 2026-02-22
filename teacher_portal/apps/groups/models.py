from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name="Guruh nomi")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_groups', verbose_name="O'qituvchi")
    total_tasks = models.IntegerField(default=75, verbose_name="Jami vazifalar soni")
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, verbose_name="Tavsif")

    class Meta:
        verbose_name = "Guruh"
        verbose_name_plural = "Guruhlar"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_student_count(self):
        return self.students.count()
