from django.test import TestCase
from rest_framework.test import APIClient
from .models import Invoice

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        data = {
            "date": "2023-07-15",
            "invoice_no": "INV-001",
            "customer_name": "Ravi",
            "details": [
                {
                    "description": "Product 1",
                    "quantity": 2,
                    "unit_price": 10.0,
                    "price": 20.0
                },
                {
                    "description": "Product 2",
                    "quantity": 3,
                    "unit_price": 15.0,
                    "price": 45.0
                }
            ]
        }
        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.first().details.count(), 2)
        # Add more assertions to test the response data

    def test_get_invoices(self):
        # Create some sample invoices
        Invoice.objects.create(date='2023-07-15', invoice_no='INV-001', customer_name='John Doe')
        Invoice.objects.create(date='2023-07-16', invoice_no='INV-002', customer_name='Jane Smith')

        response = self.client.get('/invoices/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        # Add more assertions to test the response data
