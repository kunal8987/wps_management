# Import the serializers module from Django REST Framework
from rest_framework import serializers
# Import the SKU and MSKU models from the current app's models.py
from .models import SKU, MSKU

# Define a serializer for the SKU model
class SKUSerializer(serializers.ModelSerializer):
    # Meta class to specify model and fields to include
    class Meta:
        model = SKU  # Specify the model to serialize
        fields = '__all__'  # Include all fields from the model

# Define a serializer for the MSKU model
class MSKUSerializer(serializers.ModelSerializer):
    # Meta class to specify model and fields to include
    class Meta:
        model = MSKU  # Specify the model to serialize
        fields = '__all__'  # Include all fields from the model
