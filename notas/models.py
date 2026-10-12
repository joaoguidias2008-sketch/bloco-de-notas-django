from django.conf import settings
from django.db import models


class Nota(models.Model):
    dono = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField(blank=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Nota de {self.dono}"