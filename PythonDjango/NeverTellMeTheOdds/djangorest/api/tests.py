from django.test import TestCase
from .models import SingleBet

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
                new_count = SingeBet.objects.count()
                self.assertNotEqual(old_count, new_count)

