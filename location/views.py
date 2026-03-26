from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from member.models import Member
from rest_framework import status
from member.serializer import MemberSerializer
# Create your views here.

class Demo(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        qs = Member.objects.all()
        serializer = MemberSerializer(qs, many=True)
        return Response(serializer.data)