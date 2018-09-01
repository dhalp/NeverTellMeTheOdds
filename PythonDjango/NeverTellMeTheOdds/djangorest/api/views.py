from django.shortcuts import render

from rest_framework import generics
from .serializers import SingleBetSerializer
from .models import SingleBet

class CreateView(generics.ListCreateAPIView):
        """This class defines the create behavior of our rest api."""
        queryset = SingleBet.objects.all()
        serializer_class = SingleBetSerializer

        def perform_create(self, serializer):
                """Save the post data when creating a new bucketlist."""
                serializer.save()
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
        """This class handles the http GET, PUT, and DELETE requests."""

        queryset = SingleBet.objects.all()
        serializer_class = SingleBetSerializer
      
