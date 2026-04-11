from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializer import LocationMakeSerializer, LocationSerializer,LocationListSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Location
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

# Create your views here.

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class RegisterLocation(APIView):
    permission_classes=[IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def put(self, request):
        serializer = LocationMakeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        location = serializer.save()
        return Response(LocationMakeSerializer(location).data, status=status.HTTP_201_CREATED)


class LocationDetail(APIView):
    def get(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Demostration(APIView):
    def get(self, request):
        return Response({"message": "YO man"})
    


class LcationListVIew(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationListSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes=[IsAuthenticated]