from django.db import models

class CPerfil(models.Model):
    email = models.EmailField(max_length=100, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    nickLol = models.CharField(max_length=30, null=False, blank=False)
    nickValorant = models.CharField(max_length=30, null=False, blank=False)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    pix = models.CharField(max_length=100, null=False, blank=False)
