# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='regions')
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} in {self.country.name}"

class Mammal(models.Model):
    name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    height = models.CharField(max_length=50, blank=True, null=True)
    pregnancy_period = models.CharField(max_length=50, blank=True, null=True)
    lifespan = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    diet = models.CharField(max_length=50, blank=True, null=True)
    lifestyle = models.CharField(max_length=50, blank=True, null=True)
    regions = models.ManyToManyField(Region, related_name='mammals', blank=True)

    def __str__(self):
        return self.name
