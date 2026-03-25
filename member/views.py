from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from .models import Member
from rest_framework import status
from .serializer import MemberSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class LoginView(APIView):
    def post(self, request):
        _request_body = request.data
        _member = Member.objects.filter(nickname=_request_body['nickname']).first()
        if _member:
            _tokens = get_tokens_for_user(_member)
            return Response({"tokens": _tokens}, status=status.HTTP_200_OK)
        else:
            return Response({'Didnt found'}, status=status.HTTP_404_NOT_FOUND)

class RegisterMemberView(APIView):
    def post(self, request):
        _request_body=request.data
        if Member.objects.filter(nickname=_request_body['nickname']).exists():
            return Response({"status": "Already exist"},status=status.HTTP_409_CONFLICT)
        
        _serializer = MemberSerializer(data=_request_body)
        if _serializer.is_valid():
            _serializer.save()
            return Response({"status": "Member created"},status=status.HTTP_201_CREATED) 

