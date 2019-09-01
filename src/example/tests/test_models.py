from django.test import TestCase

from example.models import Example
from .factories import ExampleFactory


class ExampleTest(TestCase):
    def setUp(self):
        super().setUp()

    def test_create_example(self):
        ExampleFactory()
        examples = Example.objects.count()

        self.assertEqual(examples, 1)

    def test_update_example(self):
        example = ExampleFactory()
        example.number = 10
        example.save()
        examples = Example.objects.filter(number=10).count()

        self.assertEqual(examples, 1)

    def test_delete_example(self):
        example = ExampleFactory()
        examples = Example.objects.count()

        self.assertEqual(examples, 1)

        example.delete()
        examples = Example.objects.count()

        self.assertEqual(examples, 0)
