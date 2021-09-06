from rest_framework import serializers
from quoteme.quotes.models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = '__all__'
