from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import ExampleSerializer
from .models import Example


class ExampleViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)

    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    http_method_names = ["get", "post"]

    def get_queryset(self):
        return self.queryset.order_by("id")
