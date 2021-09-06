from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from quoteme.quotes.lib.utils.testing_factories.quote_factories import QuoteFactory
from quoteme.quotes.models import Quote


class QuoteViewTests(APITestCase):
    def setUp(self):
        self.q1 = QuoteFactory()

    def test_GET_WithExisting_ReturnsQuote(self):
        # Arrange
        # Act
        response = self.client.get(reverse("quote", args=[self.q1.id]))

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["author"], self.q1.author)
        self.assertEqual(response.data["source"], self.q1.source)
        self.assertEqual(response.data["quote"], self.q1.quote)

    def test_PUT_WithExisting_UpdatesQuote(self):
        # Arrange
        put_data = {
            'author': 'new author',
            'source': 'new source',
            'quote': 'new quote'
        }

        # Act
        response = self.client.put(reverse("quote", args=[self.q1.id]), put_data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["author"], put_data['author'])
        self.assertEqual(response.data["source"], put_data['source'])
        self.assertEqual(response.data["quote"], put_data['quote'])


class QuoteListCreateViewTests(APITestCase):
    def setUp(self):
        self.q1 = QuoteFactory()
        self.q2 = QuoteFactory()
        self.q3 = QuoteFactory()
        self.q4 = QuoteFactory()
        self.q5 = QuoteFactory()

    def test_GET_WithExisting_ReturnAllQuotes(self):
        # Arrange
        # Act
        response = self.client.get(reverse("quotes"))

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_POST_WithValidData_CreatesQuote(self):
        # Arrange
        post_data = {
            'author': 'new author',
            'source': 'new source',
            'quote': 'new quote'
        }

        # Act
        response = self.client.post(reverse("quotes"), post_data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["author"], post_data['author'])
        self.assertEqual(response.data["source"], post_data['source'])
        self.assertEqual(response.data["quote"], post_data['quote'])

    def test_POST_WithInvalidData_Returns400(self):
        # Arrange
        post_data = {
            'none': 'new author',
            'source': 'new source',
            'quote': 'new quote'
        }

        # Act
        response = self.client.post(reverse("quotes"), post_data)

        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class QuotesBulkCreateViewTests(APITestCase):

  def test_POST_Many_CreatesQuotes(self):
        # Arrange
        post_data = [{
            'author': 'new author',
            'source': 'new source',
            'quote': 'new quote'
        } for i in range(5)]

        # Act
        response = self.client.post(reverse("quotes-bulk"), post_data, format='json')

        # Assert
        db_quotes = Quote.objects.all()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(db_quotes), 5)
