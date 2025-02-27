from rest_framework import generics, permissions
from .models import Referral
from .serializers import ReferralSerializer

class ReferralListCreateView(generics.ListCreateAPIView):
    """
    GET: List all referrals by the current user (referrer).
    POST: Create a new referral, auto-setting the referrer as the current user.
    """
    serializer_class = ReferralSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show referrals where the logged-in user is the referrer
        return Referral.objects.filter(referrer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(referrer=self.request.user)
