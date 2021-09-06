from rest_framework import generics, status
from rest_framework.views import APIView
from django.http import HttpResponse
from quoteme.quotes.models import Quote
from .serializers import QuoteSerializer


class QuotesListCreateView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


quotes_list_create_view = QuotesListCreateView.as_view()


class QuotesBulkCreateView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = QuoteSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=status.HTTP_201_CREATED)

        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


quotes_bulk_create_view = QuotesBulkCreateView.as_view()


class QuoteUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    lookup_url_kwarg = 'quote_id'


quote_update_destroy_view = QuoteUpdateDestroyView.as_view()