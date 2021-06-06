from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json
from .models import Contact

class ContctsTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new contact object.
        """
        url = reverse('contacts-list')
        data = {'first_name': 'pouya', 'last_name': 'lotfiyan'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_contact(self):
        contact = Contact()
        contact.id = 1
        contact.first_name = "pouya"
        contact.last_name = "lotfiyan"
        contact.save()
        response = self.client.get('/contacts/1/')
        self.assertEqual(response.data['id'], 1)
