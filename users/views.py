from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer,CustomUserSerializer

class RegisterAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        try:
            user = request.user
            serializer = CustomUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except (Token.DoesNotExist, AttributeError, IndexError):
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
