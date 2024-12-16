from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import AstronomicalObject, DataRelease

class AstronomicalObjectAPITest(APITestCase):
    def setUp(self):
        """
        Setup data for tests.
        Creates a DataRelease instance and two AstronomicalObject instances.
        """
        # Clean up any existing objects before the test
        AstronomicalObject.objects.all().delete()
        
        #Create DataRelease instance
        self.data_release = DataRelease.objects.create(
            name="Release A", pretty_name="First Release", version=1.0
        )

        # Create AstronomicalObject instances
        self.astro_object1 = AstronomicalObject.objects.create(
            right_ascension=150.1,
            declination=-20.5,
            source_name="Object1",
            data_release=self.data_release
        )

        self.astro_object2 = AstronomicalObject.objects.create(
            right_ascension=130.3,
            declination=-22.1,
            source_name="Object2",
            data_release=self.data_release
        )

    def test_list_astronomical_objects(self):
        """
        Test the list endpoint for astronomical objects (GET).
        """
        url = reverse('astro_objects_list')  # URL for listing all astronomical objects
        response = self.client.get(url)  # Make a GET request to this URL
        
        # Ensure the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Test that the response contains 2 objects (since we've created two in the setup)
        self.assertEqual(response.data['count'], 2)  # Expect only 2 objects
        
        # Verify that the returned objects have the expected source names
        self.assertEqual(response.data['results'][0]['Source Name'], "Object1")
        self.assertEqual(response.data['results'][1]['Source Name'], "Object2")
        

    def test_retrieve_astronomical_object(self):
        """
        Test the retrieve endpoint for an individual astronomical object (GET by ID).
        """
        url = reverse('astronomicalobject-detail', args=[self.astro_object1.id])  # URL for a specific object
        response = self.client.get(url)  # Make a GET request to retrieve the specific object
        
        # Ensure the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify that the returned object matches the one we created
        self.assertEqual(response.data['Source Name'], "Object1")
        self.assertEqual(response.data['Right Ascension'], 150.1)
        self.assertEqual(response.data['Declination'], -20.5)
        self.assertEqual(response.data['Data Release']['Pretty Name'], "First Release")

