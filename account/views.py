from .serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .permissions import IsActivePermission
from .serializers import RegistrationSerializer


class RegistrationView(APIView):

    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(
            data=data
        )
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
        return Response("Аккаунт успешно создан", status=201)


class ActivationView(APIView):

    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response(
                "Аккаунт успешно активирован", status=200
                            )


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):

    permission_classes = [IsActivePermission]

    def post(self, requests):
        user = requests.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно вышли из аккаунта')



# Если вам нужно передать requests в сериализаторы, то нужно переопределить методы get_serializer_context и get_serializer
