from rest_framework import serializers
from .models import SingleBet

class SingleBetSerializer(serializers.ModelSerializer):
        """Serializer to map the Model instance into JSON format."""

        class Meta:
                """Meta class to map serialzer's fields with the model fields."""
                model = SingleBet
                fields = ('id', 'name', 'date_created', 'date_modified')
                read_only_fields = ('date_created', 'date_modified')
