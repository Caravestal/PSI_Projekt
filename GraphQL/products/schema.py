import graphene
from graphene_django import DjangoObjectType
from .models import Nauczyciele, Lekcje, LekcjeNauczycieli


class NauczycieleType(DjangoObjectType):
    class Meta:
        model = Nauczyciele
        fields = ('pesel', 'imie', 'nazwisko, stopienNaukowy, stawkaGodzinowa')


class LekcjeType(DjangoObjectType):
    class Meta:
        model = Lekcje
        fields = (
            'id',
            'jezyk',
            'data',
            'stopien',
            'podrecznik',
        )


class LekcjeNauczycieliType(DjangoObjectType):
    class Meta:
        model = LekcjeNauczycieli
        fields = (
            'pesel',
            'idLekcji',
        )



class Query(graphene.ObjectType):
    nauczyciele = graphene.List(NauczycieleType)
    lekcje = graphene.List(LekcjeType)
    lekcjeNauczycieli = graphene.List(LekcjeNauczycieliType)

    def resolve_nauczyciele(root, info, **kwargs):
        # Querying a list
        return Nauczyciele.objects.all()

    def resolve_lekcje(root, info, **kwargs):
        # Querying a list
        return Lekcje.objects.all()

    def resolve_lekcjeNauczycieli(root, info, **kwargs):
        # Querying a list
        return LekcjeNauczycieli.objects.all()



class UpdateLekcje(graphene.Mutation):
    class Arguments:
        # Mutation to update a category
        id = graphene.ID()
        jezyk = graphene.String(required=True)
        data = graphene.Date()
        stopien = graphene.String()
        podrecznik = graphene.String()

    lekcje = graphene.Field(LekcjeType)

    @classmethod
    def mutate(cls, root, info, jezyk, data, stopien, podrecznik, id):
        lekcje = Lekcje.objects.get(pk=id)
        lekcje.jezyk = jezyk
        lekcje.data = data
        lekcje.stopien = stopien
        lekcje.podrecznik = podrecznik
        lekcje.save()

        return UpdateLekcje(lekcje=lekcje)


class CreateLekcje(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        jezyk = graphene.String(required=True)
        data = graphene.Date()
        stopien = graphene.String()
        podrecznik = graphene.String()

    # Class attributes define the response of the mutation
    lekcje = graphene.Field(LekcjeType)

    @classmethod
    def mutate(cls, root, info, jezyk, data, stopien, podrecznik, id):
        lekcje = Lekcje.objects.get(pk=id)
        lekcje.jezyk = jezyk
        lekcje.data = data
        lekcje.stopien = stopien
        lekcje.podrecznik = podrecznik
        lekcje.save()

        return CreateLekcje(lekcje=lekcje)


class NauczycieleInput(graphene.InputObjectType):
    pesel = graphene.String(required=True)
    imie = graphene.String()
    nazwisko = graphene.String()
    stopienNaukowy = graphene.String()
    stawkaGodzinowa = graphene.Int()


class CreateNauczyciele(graphene.Mutation):
    class Arguments:
        input = NauczycieleInput(required=True)

    nauczyciele = graphene.Field(NauczycieleType)

    @classmethod
    def mutate(cls, root, info, input):
        nauczyciele = Nauczyciele
        nauczyciele.pesel = input.nauczyciele
        nauczyciele.imie = input.imie
        nauczyciele.nazwisko = input.nazwisko
        nauczyciele.stopienNaukowy = input.stopienNaukowy
        nauczyciele.stawkaGodzinowa = input.stawkaGodzinowa
        nauczyciele.save()
        return CreateNauczyciele(nauczyciele=nauczyciele)


class UpdateNauczyciele(graphene.Mutation):
    class Arguments:
        input = NauczycieleInput(required=True)
        id = graphene.ID()

    nauczyciele = graphene.Field(NauczycieleType)

    @classmethod
    def mutate(cls, root, info, input, id):
        nauczyciele = Nauczyciele.objects.get(pk=id)
        nauczyciele.pesel = input.nauczyciele
        nauczyciele.imie = input.imie
        nauczyciele.nazwisko = input.nazwisko
        nauczyciele.stopienNaukowy = input.stopienNaukowy
        nauczyciele.stawkaGodzinowa = input.stawkaGodzinowa
        nauczyciele.save()
        return CreateNauczyciele(nauczyciele=nauczyciele)


class Mutation(graphene.ObjectType):
    update_lekcje = UpdateLekcje.Field()
    create_lekcje = CreateLekcje.Field()
    create_nauczyciele = CreateNauczyciele.Field()
    update_nauczyciele = UpdateNauczyciele.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)