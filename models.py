import datetime
from django.db import models
from enum import Enum

class Nauczyciele(models.Model):
    pesel = models.CharField(max_length=11, unique=True)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    stopienNaukowy = models.CharField(max_length=45)
    stawkaGodzinowa = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('pesel',)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko


class LekcjaNauczycieli(models.Model):
    pesel = models.ForeignKey(Nauczyciele, on_delete=models.CASCADE)
    idLekcji = models.ForeignKey(Lekcje, on_delete=models.CASCADE)

    class Meta:
        ordering = ('pesel',)

    def __str__(self):
        return self.pesel + ' ' + self.idLekcji

class Lekcje(models.Model):
    id = models.IntegerField()
    jezyk = models.CharField(max_length=45)
    data = models.DateField()
    stopien = models.CharField(max_length=2)
    podrecznik = models.CharField(max_length=45)

    class Meta:
        ordering = ('id',)


class LekcjeUczniow(models.Model):
    pesel = models.ForeignKey(Uczniowie, on_delete=models.CASCADE)
    idLekcji = models.ForeignKey(Lekcje, on_delete=models.CASCADE)

    class Meta:
        ordering = ('pesel',)

    def __str__(self):
        return self.pesel + ' ' + self.idLekcji

class Uczniowie(models.Model):
    pesel = models.CharField(max_length=11, unique=True)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)

    class Meta:
        ordering = ('pesel',)

class Platnosci(models.Model):
    id = models.IntegerField()
    pesel = models.ForeignKey(Uczniowie)
    semestr = models.CharField(max_length=45)
    kwota = IntegerField()
    jezyk = models.CharField(max_length=45)

    class Meta:
        ordering = ('pesel',)

    def __str__(self):
        return self.pesel + ' ' + self.kwota

class EgzaminyUczniow(models.Model):
    idEgzaminu = models.ForeignKey(Egzaminy, on_delete=models.CASCADE)
    pesel = models.ForeignKey(Uczniowie, on_delete=models.CASCADE)
    zaliczenie = models.BooleanField()

    class Meta:
        ordering = ('pesel',)

    def __str__(self):
        return self.pesel + ' ' + self.idEgzaminu + ' ' + self.zaliczenie

class Egzaminy(models.Model):
    id = models.IntegerField()
    nazwa = models.CharField(max_length=45)
    data = models.DateField()
    jezyk = models.CharField(max_length=45)
