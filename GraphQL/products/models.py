from django.db import models


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

class Lekcje(models.Model):
    id = models.IntegerField(primary_key=True)
    jezyk = models.CharField(max_length=45)
    data = models.DateField()
    stopien = models.CharField(max_length=2)
    podrecznik = models.CharField(max_length=45)

    class Meta:
        ordering = ('id',)

class LekcjeNauczycieli(models.Model):
    pesel = models.ForeignKey(Nauczyciele, on_delete=models.CASCADE)
    idLekcji = models.ForeignKey(Lekcje, on_delete=models.CASCADE)

    class Meta:
        ordering = ('pesel',)

    def __str__(self):
        return self.pesel + ' ' + self.idLekcji