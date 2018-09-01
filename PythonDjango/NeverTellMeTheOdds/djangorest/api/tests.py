from django.test import TestCase
from .models import SingleBet

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
        """This class defines the test suite for the bucketlist model."""

        def setUp(self):
                """Define the test client and other test variables."""
                self.singlebet_name = "Test Bet"
                self.singlebet = SingleBet(name=self.singlebet_name)

        def test_model_can_create_a_singlebet(self):
                """Test the singlebet model can create a singlebet."""
                old_count = SingleBet.objects.count()
                self.singlebet.save()
                new_count = SingleBet.objects.count()
                self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
        """Test suite for the api views."""

        def setUp(self):
          """Define the test client and other test variables."""
          self.client = APIClient()
          self.bucketlist_data = {'name': 'Nathan Horesh'}
          self.response = self.client.post(
                          reverse('create'),
                          self.bucketlist_data,
                          format="json")

        def test_api_can_create_a_singlebet(self):
                """Test the api has bet creation capablilty."""
                self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

       def test_api_can_get_a_singlebet(self):
               """Test the api can get a given singlebet."""
               singlebet = SingleBet.objects.get()
               response = self.client.gert(
                  reverse('details',
                          kwargs={'pk': singlebet.id}), format="json")
              
              self.assertEqual(response.status_code, status.HTTP_200_OK)
              self.assertContains(response, singlebet)

       def test_api_can_update_singlebet(self):
               """Test the api can update a given bet."""
              change_singlebet = {'name': 'Something New'}
              res = self.client.put(
                  reverse('details', kwargs={'pk': singlebet.id}),
                  change_singlebet, format='json'
              )
              self.assertEqual(res.status_code, status.HTTP_200_OK)

      def test_api_can_delete_singlebet(self):
              """Test the api can delete bet."""
              singlebet = SingleBet.objects.get()
              response = self.client.delete(
                  reverse('details', kwargs={'pk': singlebet.id}),
                  format='json',
                  follow=True)

              self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
