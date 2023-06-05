from django.test import TestCase
from .models import *

# Create your tests here.
class MyAPITestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='Example Company',
            location='Example Location',
            about='Example about',
            type='IT',
            active=True
        )

    def test_companies_get(self):
        # Make a request to your API
        response = self.client.get('/companies/')
        self.assertEqual(response.status_code, 200)

    def test_employees_get(self):
        # Make a request to your API
        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, 200)

    def test_companies_post(self):
        
        data = {
            'name': 'ExampleCompany',
            'location': 'Example Location',
            'about': 'Example about',
            'type': 'IT',
            'active': True
        }

        # Make a request to your API
        response = self.client.post('/companies/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Company.objects.filter(name='ExampleCompany').exists())
        
    def test_employees_post(self):
        data = {
            'name': 'John Doe',
            'email': 'test@test.com',
            'address': 'Example Address',
            'phone': '1234567890',
            'about': 'Example about',
            'position': 'Manager',
            'company': self.company.company_id
        }

        # Make a request to your API
        response = self.client.post('/employees/', data, format='json')
        self.assertTrue(Employee.objects.filter(name='John Doe').exists())
        self.assertEqual(response.status_code, 201)

    def test_employees_post_wrong_companyid(self):
        data = {
            'name': 'John Doe',
            'email': 'test@test.com',
            'address': 'Example Address',
            'phone': '1234567890',
            'about': 'Example about',
            'position': 'Manager',
            'company': 1212
        }

        # Make a request to your API
        response = self.client.post('/employees/', data, format='json')
        self.assertEqual(response.status_code, 400)

    