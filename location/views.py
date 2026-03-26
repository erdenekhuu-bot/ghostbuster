from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializer import LocationSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# Create your views here.


class RegisterLocation(APIView):
    permission_classes=[IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def put(self, request):
        serializer = LocationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        location = serializer.save()
        return Response(LocationSerializer(location).data, status=status.HTTP_201_CREATED)
