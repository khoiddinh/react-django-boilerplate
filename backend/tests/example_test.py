from django.test import TestCase
from rest_framework.test import APIClient

# Uses Django’s built-in TestCase + DRF’s APIClient
# Run Tests with: python manage.py test
class ExampleRouteTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_root_route(self):
        response = self.client.get("/api/hello/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "Hello World"})