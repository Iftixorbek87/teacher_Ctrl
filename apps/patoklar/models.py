from django.db import models
from django.contrib.auth.models import User


class Patok(models.Model):
    nomi = models.CharField(max_length=150, verbose_name="Patok nomi")
    oqituvchi = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='patoklar',
        verbose_name="O'qituvchi"
    )
    tavsif = models.TextField(blank=True, verbose_name="Tavsif")
    yaratilgan = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Patok"
        verbose_name_plural = "Patoklar"
        ordering = ['-yaratilgan']

    def __str__(self):
        return self.nomi

    def guruhlar_soni(self):
        return self.guruhlar.count()

    def talabalar_soni(self):
        from apps.talabalar.models import Talaba
        return Talaba.objects.filter(guruh__patok=self).count()
