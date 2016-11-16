from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

class SnippetList(APIView):
    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)