# -*- coding: utf-8 -*-
from django.db import models

class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    producto = models.TextField('Producto', blank=True)
    lote = models.TextField('Lote', max_length=100)
    datecompra = models.TextField('Date compra', max_length=100)
    description = models.TextField('Description', blank=True)
    # img = models.FileField()
    evidencia = models.TextField('Evidencia', blank=True)
    price = models.DecimalField('Cantidad', decimal_places=2, max_digits=8)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})
