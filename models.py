import datetime
from enum import Enum

class Nauczyciele:
    pesel: str
    imie: str
    nazwisko: str
    stopienNaukowy: str
    stawkaGodzinowa: int

class LekcjaNauczycieli:
    pesel: str
    idLekcji: int

class Lekcje:
    id: int
    jezyk: str
    data: datetime.date
    stopien: Enum
    podrecznik: str

class LekcjeUczniow:
    pesel: str
    idLekcji: int

class Uczniowie:
    pesel: str
    imie: str
    nazwisko: str

class Platnosci:
    id: int
    pesel: str
    semestr: str
    kwota: int
    jezyk: str

class EgzaminyUczniow:
    idEgzaminu: int
    pesel: str
    zaliczenie: bool

class Egzaminy:
    id: int
    nazwa: str
    data: datetime.date
    jezyk: str
