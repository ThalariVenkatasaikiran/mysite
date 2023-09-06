from .models import Email

from .serializers import EmailSerializer
from .serializers import EmailSerializer, DummyEmailSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404



class EmailList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        emails = Email.objects.all()


    def get_object(self, pk):
        try:
            return Email.objects.get(pk=pk)
        except Email.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if not pk:
            emails = Email.objects.all()
        else:
            emails = [self.get_object(pk)]
        serializer = EmailSerializer(emails, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        import pdb;pdb.set_trace()
        email = self.get_object(pk)
        serializer = EmailSerializer(email, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        import pdb;pdb.set_trace()
        email = self.get_object(pk)
        serializer = DummyEmailSerializer(email, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        import pdb;pdb.set_trace()
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
