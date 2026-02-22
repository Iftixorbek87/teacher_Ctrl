from django.db import models
from apps.patoklar.models import Patok


class Guruh(models.Model):
    patok = models.ForeignKey(
        Patok, on_delete=models.CASCADE,
        related_name='guruhlar',
        verbose_name="Patok"
    )
    nomi = models.CharField(max_length=150, verbose_name="Guruh nomi")
    jami_vazifalar = models.IntegerField(default=75, verbose_name="Jami vazifalar soni")
    tavsif = models.TextField(blank=True, verbose_name="Tavsif")
    yaratilgan = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Guruh"
        verbose_name_plural = "Guruhlar"
        ordering = ['nomi']

    def __str__(self):
        return f"{self.patok.nomi} / {self.nomi}"

    def talabalar_soni(self):
        return self.talabalar.count()
