from rest_framework import status, viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Email
from .serializers import EmailSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer