from django.test import TestCase
from rest_framework.test import APIClient


class SampleTest(TestCase):
    client = APIClient()

    def test_get(self):
        response = self.client.get('/sample/')
        self.assertDictEqual(response.data, {'method': 'get'}, '[GET] /sample: unexpected result')

    def test_post(self):
        response = self.client.post('/sample/')
        self.assertDictEqual(response.data, {'method': 'post'}, '[POST] /sample: unexpected result')

    def test_put(self):
        response = self.client.put('/sample/')
        self.assertDictEqual(response.data, {'method': 'put'}, '[PUT] /sample: unexpected result')

    def test_delete(self):
        response = self.client.delete('/sample/')
        self.assertDictEqual(response.data, {'method': 'delete'}, '[DELETE] /sample: unexpected result')