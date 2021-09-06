from factory.django import DjangoModelFactory
import factory.fuzzy
from quoteme.quotes.models import Quote


class QuoteFactory(DjangoModelFactory):
    class Meta:
        model = Quote

    author = factory.sequence(lambda n: f'Title for post {n}')
    source = factory.sequence(lambda n: f'HTML for post {n}')
    quote = factory.sequence(lambda n: f'HTML for post {n}')
