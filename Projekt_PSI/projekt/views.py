from django.http import HttpResponse
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Nauczyciele, LekcjeNauczycieli, Lekcje, LekcjeUczniow, Uczniowie, Platnosci, EgzaminyUczniow, Egzaminy
from .serializers import NauczycieleSerializer, LekcjeSerializer, LekcjeNauczycieliSerializer, LekcjeUczniowSerializer, UczniowieSerializer, EgzaminySerializer, EgzaminyUczniowSerializer, PlatnosciSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User
from .custompermission import IsCurrentUserOwnerOrReadOnly


class NauczycieleList(generics.ListCreateAPIView):
    queryset = Nauczyciele.objects.all()
    serializer_class = NauczycieleSerializer
    name = 'Nauczyciele-list'
    filterset_fields = ['pesel']
    search_fields = ['pesel']
    ordering_fields = ['pesel']


class NauczycieleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nauczyciele.objects.all()
    serializer_class = NauczycieleSerializer
    name = 'Nauczyciele-detail'

class NauczycieleFilter(FilterSet):
    min_stawkaGodzinowa = NumberFilter(field_name='stawkaGodzinowa', lookup_expr='gte')
    max_stawkaGodzinowa = NumberFilter(field_name='stawkaGodzinowa', lookup_expr='lte')

    class Meta:
        model = Nauczyciele
        fields = ['min_stawkaGodzinowa', 'max_stawkaGodzinowa']

class LekcjeNauczycieliList(generics.ListCreateAPIView):
    queryset = LekcjeNauczycieli.objects.all()
    serializer_class = LekcjeNauczycieliSerializer
    name = 'LekcjaNauczycieli-list'
    filter_fields = ['pesel', 'idLekcji']
    search_fields = ['pesel', 'idLekcji']
    ordering_fields = ['pesel']


class LekcjeNauczycieliDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LekcjeNauczycieli.objects.all()
    serializer_class = LekcjeNauczycieliSerializer
    name = 'LekcjeNauczycie-detail'

class LekcjeList(generics.ListCreateAPIView):
    queryset = Lekcje.objects.all()
    serializer_class = LekcjeSerializer
    name = 'Lekcje-list'
    filter_fields = ['id']
    search_fields = ['id']
    ordering_fields = ['id']

class LekcjeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lekcje.objects.all()
    serializer_class = LekcjeSerializer
    name = 'Lekcje-detail'

class LekcjeUczniowList(generics.ListCreateAPIView):
    queryset = LekcjeUczniow.objects.all()
    serializer_class = LekcjeUczniowSerializer
    name = 'LekcjeUczniow-list'
    filter_fields = ['pesel', 'idLekcji']
    search_fields = ['pesel', 'idLekcji']
    ordering_fields = ['pesel']


class LekcjeUczniowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LekcjeUczniow.objects.all()
    serializer_class = LekcjeUczniowSerializer
    name = 'LekcjeUczniow-detail'

class UczniowieList(generics.ListCreateAPIView):
    queryset = Uczniowie.objects.all()
    serializer_class = UczniowieSerializer
    name = 'Uczniowie-list'
    filterset_fields = ['pesel']
    search_fields = ['pesel']
    ordering_fields = ['pesel']


class UczniowieDetail(generics.RetrieveAPIView):
    queryset = Uczniowie.objects.all()
    serializer_class = UczniowieSerializer
    name = 'Uczniowie-detail'

class EgzaminyList(generics.ListCreateAPIView):
    queryset = Egzaminy.objects.all()
    serializer_class = EgzaminySerializer
    name = 'Egzaminy-list'
    filterset_fields = ['id']
    search_fields = ['id']
    ordering_fields = ['id']


class EgzaminyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Egzaminy.objects.all()
    serializer_class = EgzaminySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly,)
    name = 'Egzaminy-detail'

class EgzaminyFilter(FilterSet):
    froM = DateTimeFilter(field_name='data', lookup_expr='gte')
    tO = DateTimeFilter(field_name='data', lookup_expr='lte')

    class Meta:
        model = Egzaminy
        fields = ['froM', 'tO']


class EgzaminyUczniowList(generics.ListCreateAPIView):
    queryset = EgzaminyUczniow.objects.all()
    serializer_class = EgzaminyUczniowSerializer
    name = 'EgzaminyUczniow-list'
    filterset_fields = ['idEgzaminu', 'pesel']
    search_fields = ['idEgzaminu', 'pesel']
    ordering_fields = ['idEgzaminu']


class EgzaminyUczniowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EgzaminyUczniow.objects.all()
    serializer_class = EgzaminyUczniowSerializer
    name = 'EgzaminyUczniow-detail'

class PlatnosciList(generics.ListCreateAPIView):
    queryset = Platnosci.objects.all()
    serializer_class = PlatnosciSerializer
    name = 'Platnosci-list'
    filterset_fields = ['id', 'pesel']
    search_fields = ['id', 'pesel']
    ordering_fields = ['pesel']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PlatnosciDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platnosci.objects.all()
    serializer_class = PlatnosciSerializer
    name = 'Platnosci-detail'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'Nauczyciele': reverse(NauczycieleList.name, request=request),
                         'LekcjeNauczycieli': reverse(LekcjeNauczycieliList.name, request=request),
                         'Lekcje': reverse(LekcjeList.name, request=request),
                         'LekcjeUczniow': reverse(LekcjeUczniowList.name, request=request),
                         'Platnosci': reverse(PlatnosciList.name, request=request),
                         'EgzaminyUczniow': reverse(EgzaminyUczniowList.name, request=request),
                         'Egzaminy': reverse(EgzaminyList.name, request=request),
})

def strona(request):
    return HttpResponse('strona')

def onas(request):
    return HttpResponse('onas')