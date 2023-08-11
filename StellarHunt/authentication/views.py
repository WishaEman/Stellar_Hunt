from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED


class LoginView(APIView):
    """
        This view provides a post request to login a user.
    """
    serializer_class = LogInSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({
                'status': HTTP_200_OK,
                'token': token.key,
            })
        return Response({
            'status': HTTP_400_BAD_REQUEST,
            'message': 'Invalid Credentials'
        })


class SignupView(CreateAPIView):
    """
            This view provides a post request to create a user.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        if user:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({
                'status': HTTP_201_CREATED,
                'token': token.key,
            })
        return Response({
            'status': HTTP_400_BAD_REQUEST,
            'message': 'Invalid Credentials'
        })


class LogoutView(APIView):
    """
            This view provides a get request to logout a user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            'status': HTTP_200_OK,
            'message': 'Successfully Logged out User'
        })
