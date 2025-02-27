from django.urls import path
from .views import ReferralListCreateView

urlpatterns = [
    path('', ReferralListCreateView.as_view(), name='referral_list_create'),
]
