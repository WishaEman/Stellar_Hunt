from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


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
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            'status': HTTP_200_OK,
            'message': 'Successfully Logged out User'
        })


class CheckUsernameEmailView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')

        if not username or not email:
            return Response({'error': 'Username and email are required.'}, status=HTTP_400_BAD_REQUEST)

        username_exists = User.objects.filter(username=username).exists()
        email_exists = User.objects.filter(email=email).exists()

        response_data = {
            'username_taken': username_exists,
            'email_taken': email_exists,
        }

        return Response(response_data, status=HTTP_200_OK)
