from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Contract
from .serializers import ContractDetailSerializer, ContractListSerializer


class ContractList(generics.ListAPIView):
    """
    GET
    List all contracts of a given Customer (ID) as JSON List
    """
    serializer_class = ContractListSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Contract.objects.filter(customer_id=customer_id)


class ContractDetail(generics.RetrieveUpdateAPIView):
    """
    GET/POST
    Returns contract details as JSON Object
    """
    serializer_class = ContractDetailSerializer

    def get_object(self):
        customer_id = self.kwargs['customer_id']
        contract_id = self.kwargs['contract_id']
        return get_object_or_404(Contract, id=contract_id, customer_id=customer_id)
