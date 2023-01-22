from rest_framework import serializers
from .models import Nauczyciele, LekcjeNauczycieli, Lekcje, LekcjeUczniow, Uczniowie, Platnosci, EgzaminyUczniow, Egzaminy
from django.contrib.auth.models import User

class NauczycieleSerializer(serializers.HyperlinkedModelSerializer):
    LekcjeNauczycieli = serializers.SlugRelatedField(queryset=LekcjeNauczycieli.objects.all(), slug_field='pesel, idLekcji')

    class Meta:
        model = Nauczyciele
        fields = ['pesel', 'url', 'imie', 'nazwisko', 'stopienNaukowy', 'stawkaGodzinowa']

class LekcjeSerializer(serializers.HyperlinkedModelSerializer):
    LekcjeNauczycieli = serializers.SlugRelatedField(queryset=LekcjeNauczycieli.objects.all(), slug_field='pesel, idLekcji')
    LekcjeUczniow = serializers.SlugRelatedField(queryset=LekcjeUczniow.objects.all(), slug_field='idLekcji, pesel')

    class Meta:
        model = Lekcje
        fields = ['url', 'id', 'jezyk', 'data', 'stopien', 'podrecznik']

class LekcjeNauczycieliSerializer(serializers.HyperlinkedModelSerializer):
    Nauczyciele = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Nauczyciele-detail')
    Lekcje = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Lekcje-detail')
    class Meta:
        model = LekcjeNauczycieli
        fields = ['url', 'pesel', 'idLekcji']

class LekcjeUczniowSerializer(serializers.HyperlinkedModelSerializer):
    Uczniowie = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Uczniowie-detail')
    Lekcje = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Lekcje-detail')

    class Meta:
        model = LekcjeUczniow
        fields = ['url', 'pesel', 'idLekcji']

class UczniowieSerializer(serializers.HyperlinkedModelSerializer):
    LekcjeUczniow = serializers.SlugRelatedField(queryset=LekcjeUczniow.objects.all(), slug_field='idLekcji, pesel')
    EgzaminyUczniow = serializers.SlugRelatedField(queryset=EgzaminyUczniow.objects.all(), slug_field='idEgzaminu, pesel')
    Platnosci = serializers.SlugRelatedField(queryset=Platnosci.objects.all(), slug_field='id')
    class Meta:
        model = Uczniowie
        fields = ['pesel', 'url', 'imie', 'nazwisko']

class EgzaminySerializer(serializers.HyperlinkedModelSerializer):
    EgzaminyUczniow = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='EgzaminyUczniow-detail')

    class Meta:
        model = Egzaminy
        fields = ['url', 'id', 'nazwa', 'data', 'jezyk']

class EgzaminyUczniowSerializer(serializers.HyperlinkedModelSerializer):
    Uczniowie = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Uczniowie-detail')
    Egzaminy = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Egzaminy-detail')

    class Meta:
        model = EgzaminyUczniow
        fields = ['url', 'pesel', 'idEgzaminu']

class PlatnosciSerializer(serializers.HyperlinkedModelSerializer):
    Uczniowie = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Uczniowie-detail')

    class Meta:
        model = Egzaminy
        fields = ['url', 'id', 'pesel', 'semestr', 'kwota', 'jezyk']
