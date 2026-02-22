from django.db import models
from apps.guruhlar.models import Guruh


class Talaba(models.Model):
    guruh = models.ForeignKey(
        Guruh, on_delete=models.CASCADE,
        related_name='talabalar',
        verbose_name="Guruh"
    )
    ism_familya = models.CharField(max_length=200, verbose_name="Ism-familya")
    telefon     = models.CharField(max_length=20,  blank=True, default='', verbose_name="Telefon raqami")
    telegram    = models.CharField(max_length=100, blank=True, default='', verbose_name="Telegram username")
    yaratilgan  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"
        ordering = ['ism_familya']

    def __str__(self):
        return self.ism_familya

    def bajarilgan_soni(self):
        return self.vazifalar.filter(bajarildi=True).count()

    def foiz(self):
        jami = self.guruh.jami_vazifalar
        if jami == 0:
            return 0
        return round((self.bajarilgan_soni() / jami) * 100)

    def bitirdimi(self):
        return self.bajarilgan_soni() >= self.guruh.jami_vazifalar


class VazifaBajarish(models.Model):
    talaba = models.ForeignKey(
        Talaba, on_delete=models.CASCADE,
        related_name='vazifalar'
    )
    vazifa_raqam = models.IntegerField(verbose_name="Vazifa raqami")
    bajarildi    = models.BooleanField(default=False)
    vaqt         = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ['talaba', 'vazifa_raqam']
        ordering = ['vazifa_raqam']

    def __str__(self):
        return f"{self.talaba.ism_familya} — {self.vazifa_raqam}"
