from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Member
from rest_framework import status
from .serializer import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

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
        _member = User.objects.filter(username=_request_body['username']).first()
        if _member:
            _tokens = get_tokens_for_user(_member)
            return Response({"tokens": _tokens}, status=status.HTTP_200_OK)
        else:
            return Response({'Didnt found'}, status=status.HTTP_404_NOT_FOUND)

class RegisterMemberView(APIView):
    def post(self, request):
        _request_body=request.data

        if User.objects.filter(username=_request_body['username']).exists():
            return Response({"status": "Already exist"},status=status.HTTP_409_CONFLICT)
        
        _user_serializer = UserSerializer(data={
            'username': _request_body['username'],
            'password': _request_body['password'],
        })
        if not _user_serializer.is_valid():
            return Response(_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user =_user_serializer.save()

        Member.objects.create(
            user=user,
            phone=_request_body['phone'],
        )

        return Response({"status": "Member created"}, status=status.HTTP_201_CREATED)
    
    

class RemoveMemberView(APIView):
    permission_classes=[IsAuthenticated]
    def delete(self, request,pk):
        member = get_object_or_404(User, pk=pk)
        member.delete()
        return Response(status=status.HTTP_202_ACCEPTED)