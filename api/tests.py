from rest_framework.test import APITestCase
from django.test import Client
from api.models import Table


class TestTable(APITestCase):
    def setUp(self):
        self.client = Client()
        Table.objects.create(value='test_1', x_axis=0, y_axis=0)

    def test_get_table(self):
        url = '/api/table/get_table/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_table(self):
        url = '/api/table/edit_table/'
        data = {'x_axis': 1, 'y_axis': 2, 'value': 'test_2'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
