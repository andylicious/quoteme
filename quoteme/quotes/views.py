from rest_framework import generics
from quoteme.quotes.models import Quote
from .serializers import QuoteSerializer


class QuotesListCreateView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


quotes_list_create_view = QuotesListCreateView.as_view()


class QuoteUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    lookup_url_kwarg = 'quote_id'


quote_update_destroy_view = QuoteUpdateDestroyView.as_view()