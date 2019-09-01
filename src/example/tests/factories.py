from django.utils.timezone import datetime
from factory.django import DjangoModelFactory

from example.models import Example


class ExampleFactory(DjangoModelFactory):
    class Meta:
        model = Example

    number = 1
    short_text = "some text"
    long_text = "long test"
    some_date = datetime.now().date()
    boolean = False
