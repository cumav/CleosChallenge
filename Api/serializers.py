from rest_framework import serializers
from .models import Contract


class ContractDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class ContractListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id']  # Only show contract IDs

