from django.utils.timezone import date
from factory.django import DjangoModelFactory

from example.models import Example


class ExampleFactory(DjangoModelFactory):
    class Meta:
        model = Example

    number = 1
    short_text = "some text"
    long_text = "long test"
    some_date = date.today()
    boolean = False
