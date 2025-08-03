from rest_framework import status, generics  # Import status codes and generic views from DRF
from rest_framework import permissions  # Import permissions for view access control
from rest_framework.response import Response  # Import Response for API responses
from django.contrib.auth.models import User  # Import Django's built-in User model
from django.utils.translation import gettext as _  # Import translation utility for messages
from .models import SKU, MSKU  # Import SKU and MSKU models from current app
from .serializers import SKUSerializer, MSKUSerializer  # Import serializers for SKU and MSKU

# SKU Views
class SKUListCreateView(generics.ListCreateAPIView):  # View for listing and creating SKUs
    queryset = SKU.objects.all()  # Define queryset for all SKU objects
    serializer_class = SKUSerializer  # Specify serializer for SKU

class SKUDetailView(generics.RetrieveUpdateDestroyAPIView):  # View for retrieving, updating, deleting SKU
    queryset = SKU.objects.all()  # Define queryset for all SKU objects
    serializer_class = SKUSerializer  # Specify serializer for SKU

# MSKU Views
class MSKUListCreateView(generics.ListCreateAPIView):  # View for listing and creating MSKUs
    queryset = MSKU.objects.all()  # Define queryset for all MSKU objects
    serializer_class = MSKUSerializer  # Specify serializer for MSKU

class MSKUDetailView(generics.RetrieveUpdateDestroyAPIView):  # View for retrieving, updating, deleting MSKU
    queryset = MSKU.objects.all()  # Define queryset for all MSKU objects
    serializer_class = MSKUSerializer  # Specify serializer for MSKU

def is_username_taken(username):  # Utility function to check if username exists
    return User.objects.filter(username=username).exists()  # Return True if username exists

# Define a view for user registration
class UserRegistrationView(generics.CreateAPIView):  # View for user registration
    permission_classes = [permissions.AllowAny]  # Allow any user to access this view

    def post(self, request):  # Handle POST requests for registration
        username = request.data.get("username")  # Get username from request data
        password = request.data.get("password")  # Get password from request data
        if User.objects.filter(username=username).exists():  # Check if username already exists
            return Response(  # Return error response if username exists
                {"error": _("Username already exists.")},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = User.objects.create_user(username=username, password=password)  # Create new user
        return Response(  # Return success response
            {"message": _("User  registered successfully.")},
            status=status.HTTP_201_CREATED,
        )
