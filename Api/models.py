from django.db import models
from simple_history.models import HistoricalRecords


class Customer(models.Model):
    id = models.AutoField(primary_key=True)  # Continuous integer


class Contract(models.Model):
    customer = models.ForeignKey(Customer, related_name='contracts', on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=50, unique=True)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    history = HistoricalRecords()