# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class conta(models.Model):
    EST = (
        ('1', 'Aberto'),
        ('2', 'Paga'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=300)
    desc = models.CharField(max_length=300, null=True, blank=True)
    estado = models.CharField(max_length=1, choices=EST, default=1)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_venc = models.DateTimeField(default=timezone.now)
    data_cad = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome