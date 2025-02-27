from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, MeView

urlpatterns = [
    # Register endpoint
    path('register/', RegisterView.as_view(), name='register'),

    # JWT login & token refresh
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Get current user data
    path('me/', MeView.as_view(), name='me'),
]
