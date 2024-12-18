from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Contract
from .serializers import ContractDetailSerializer, ContractListSerializer


class ContractList(generics.ListAPIView):
    """
    GET
    List all contracts of a given Customer (ID) as JSON List
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ContractListSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Contract.objects.filter(customer_id=customer_id)


class ContractDetail(generics.RetrieveUpdateAPIView):
    """
    GET/POST
    Returns contract details as JSON Object
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ContractDetailSerializer

    def get_object(self):
        customer_id = self.kwargs['customer_id']
        contract_id = self.kwargs['contract_id']
        return get_object_or_404(Contract, id=contract_id, customer_id=customer_id)


class Login(APIView):
    permission_classes = [AllowAny]
    parser_classes = [JSONParser]

    def get(self, request):
        """
        Display HTML when visiting url in Browser
        """
        return render(request, 'api/login.html')

    def post(self, request):
        """
        Expecting:
        {"username": "username", "password": "password"}
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({
                'error': 'Bitte Benutzername und Passwort angeben',
                'details': {
                    'username': 'Erforderlich' if not username else None,
                    'password': 'Erforderlich' if not password else None
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({
                'error': 'Ungültige Anmeldedaten'
            }, status=status.HTTP_401_UNAUTHORIZED)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return Response({
            'status': 'success',
            'data': {
                'token': str(refresh.access_token),
                'user': user.pk,
            }
        }, status=status.HTTP_200_OK)


def frontend(request):
    """
    Renders simple HTML frontend
    """
    return render(request, 'api/frontend.html')
