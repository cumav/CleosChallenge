from rest_framework import serializers
from .models import Contract


class ContractHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract.history.model  # Access the historical model created by django-simple-history
        fields = ['contract_number', 'premium', 'customer']  # Avoid unused history data


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
    last_history = serializers.SerializerMethodField()  # 1. Define last_history

    class Meta:
        model = Contract
        fields = '__all__'

    def get_last_history(self, obj):
        """
        Retrieve the latest history entry. #
        Django passes the result from 'get_last_history' into previous defined 'last_history'.
        """
        history_queryset = obj.history.all()
        if history_queryset.count() > 1:
            second_latest_history = history_queryset[1]  # Index for the second entry
            return ContractHistorySerializer(second_latest_history).data
        return None
