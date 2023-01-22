from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from . import views
from .models import Nauczyciele, Egzaminy
from rest_framework import status
from django import urls
from django.contrib.auth.models import User
import datetime

class Nauczyciele(APITestCase):
    def create_Nauczyciele(self, pesel, imie, nazwisko, stopienNaukowy, stawkaGodzinowa):
        url = reverse(views.NauczycieleList.name)
        data = {'pesel': pesel,
                'imie': imie,
                'nazwisko': nazwisko,
                'stopienNaukowy': stopienNaukowy,
                'stawkaGodzinowa': stawkaGodzinowa, }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_Nauczyciele(self):
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        client = APIClient()
        client.login(username='admin', password='admin123')
        new_pesel = '88121256941'
        new_imie = 'Racibor'
        new_nazwisko = 'Nowak'
        new_stopienNaukowy = 'dr'
        new_stawkaGodzinowa = '30'
        response = self.create_Nauczyciele(new_pesel, new_imie, new_nazwisko, new_stopienNaukowy, new_stawkaGodzinowa, client)
        assert response.status_code == status.HTTP_201_CREATED
        assert Nauczyciele.objects.count() == 1
        assert Nauczyciele.objects.get().imie == new_imie
        assert Nauczyciele.objects.get().nazwisko == new_nazwisko

class EgzaminyTests(APITestCase):
    def post_Egzaminy(self, id, nazwa, data, jezyk):
        url = reverse(views.NauczycieleList.name)
        data = {'id': id,
                'nazwa': nazwa,
                'data': data,
                'jezyk': jezyk, }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_Egzaminy(self):
        new_id = 44
        new_nazwa = 'SerbskiB2'
        new_data = datetime.strptime('2023-05-12', '%Y-%m-%d').date()
        new_jezyk = 'serbski'
        response = self.post_Egzaminy(new_id,new_nazwa,new_data,new_jezyk)
        print("PK {0}".format(Egzaminy.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Egzaminy.objects.count() == 1
        assert Egzaminy.objects.get().id == new_id
        assert Egzaminy.objects.get().nazwa == new_nazwa
        assert Egzaminy.objects.get().data == new_data
        assert Egzaminy.objects.get().jezyk == new_jezyk

    def test_update_Egzaminy(self):
        egzaminy_id = 44
        egzaminy_nazwa = 'SerbskiB2'
        egzaminy_data = datetime.strptime('2023-05-12', '%Y-%m-%d').date()
        egzaminy_jezyk = 'serbski'
        response = self.post_Egzaminy(egzaminy_id,egzaminy_nazwa,egzaminy_data,egzaminy_jezyk)
        url = urls.reverse(views.EgzaminyDetail.name,None,{response.data['pk']})
        updated_id = 44
        updated_nazwa = 'SerbskiB2'
        updated_data = datetime.strptime('2023-05-23', '%Y-%m-%d').date()
        updated_jezyk = 'serbski'
        data = {'id': updated_id,
                'nazwa': updated_nazwa,
                'data': updated_data,
                'jezyk': updated_jezyk, }
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['id'] == updated_id
        assert patch_response.data['nazwa'] == updated_nazwa
        assert patch_response.data['data'] == updated_data
        assert patch_response.data['jezyk'] == updated_jezyk

    def test_get_book_category(self):
        egzaminy_id = 44
        egzaminy_nazwa = 'SerbskiB2'
        egzaminy_data = datetime.strptime('2023-05-12', '%Y-%m-%d').date()
        egzaminy_jezyk = 'serbski'
        response = self.post_Egzaminy(egzaminy_id,egzaminy_nazwa,egzaminy_data,egzaminy_jezyk)
        url = urls.reverse(views.EgzaminyDetail.name,None,{response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['id'] == egzaminy_id
        assert get_response.data['nazwa'] == egzaminy_nazwa
        assert get_response.data['data'] == egzaminy_data
        assert get_response.data['jezyk'] == egzaminy_jezyk


