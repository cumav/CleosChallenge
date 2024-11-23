from rest_framework import serializers
from .models import Contract


class ContractDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

    def validate_premium(self, value):
        """
        Make sure the premium is valid
        """
        if value <= 0:
            raise serializers.ValidationError("Premium must be positive.")
        return value


class ContractListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
