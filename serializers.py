from rest_framework import serializers
from .models import Order, Book, BookCategory, Client
from django.contrib.auth.models import User

class NauczycieleSerializer(serializers.HyperlinkedModelSerializer):
    nauczyciele = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='nauczyciele-detail')

    class Meta:
        model = Nauczyciele
        fields = ['pesel', 'url', 'imie', 'nazwisko', 'stopienNaukowy', 'stawkaGodzinowa']

class LekcjeSerializer(serializers.HyperlinkedModelSerializer):
    lekcje = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Lekcje-detail')

    class Meta:
        model = Lekcje
        fields = ['url', 'id', 'jezyk', 'data', 'stopien', 'podrecznik']

class LekcjaNauczycieliSerializer(serializers.HyperlinkedModelSerializer):
    lekcjaNauczycieli = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='lekcjaNauczycieli-detail')
    pesel = serializers.SlugRelatedField(queryset=Nauczyciele.objects.all(), slug_field='pesel')
    idLekcji = serializers.SlugRelatedField(queryset=Lekcje.objects.all(), slug_field='id')
    class Meta:
        model = LekcjaNauczycieli
        fields = ['url', 'pesel', 'idLekcji']

class LekcjeUczniowSerializer(serializers.HyperlinkedModelSerializer):
    lekcjaUczniow = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='lekcjaUczniow-detail')
    pesel = serializers.SlugRelatedField(queryset=Uczniowie.objects.all(), slug_field='pesel')
    idLekcji = serializers.SlugRelatedField(queryset=Lekcje.objects.all(), slug_field='id')

    class Meta:
        model = LekcjeUczniow
        fields = ['url', 'pesel', 'idLekcji']

class UczniowieSerializer(serializers.HyperlinkedModelSerializer):
    uczniowie = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='uczniowie-detail')

    class Meta:
        model = Uczniowie
        fields = ['pesel', 'url', 'imie', 'nazwisko']

class EgzaminySerializer(serializers.HyperlinkedModelSerializer):
    egzaminy = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='egzaminy-detail')

    class Meta:
        model = Egzaminy
        fields = ['url', 'id', 'nazwa', 'data', 'jezyk']

class EgzaminyUczniowSerializer(serializers.HyperlinkedModelSerializer):
    egzaminyUczniow = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='egzaminyUczniow-detail')
    pesel = serializers.SlugRelatedField(queryset=Uczniowie.objects.all(), slug_field='pesel')
    idEgzaminu = serializers.SlugRelatedField(queryset=Egzaminy.objects.all(), slug_field='id')

    class Meta:
        model = EgzaminyUczniow
        fields = ['url', 'pesel', 'idEgzaminu']

class PlatnosciSerializer(serializers.HyperlinkedModelSerializer):
    platnosci = serializers.ypHerlinkedRelatedField(many=True, read_only=True, view_name='platnosci-detail')
    pesel = serializers.SlugRelatedField(queryset=Uczniowie.objects.all(), slug_field='pesel')

    class Meta:
        model = Egzaminy
        fields = ['url', 'id', 'pesel', 'semestr', 'kwota', 'jezyk']
