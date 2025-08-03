from django.urls import path
from .views import (
    SKUListCreateView,
    SKUDetailView,
    MSKUListCreateView,
    MSKUDetailView,
    UserRegistrationView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("skus/", SKUListCreateView.as_view(), name="sku-list-create"),
    path("skus/<int:pk>/", SKUDetailView.as_view(), name="sku-detail"),
    path("mskus/", MSKUListCreateView.as_view(), name="msku-list-create"),
    path("mskus/<int:pk>/", MSKUDetailView.as_view(), name="msku-detail"),
]
