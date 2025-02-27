from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from .models import Referral

User = get_user_model()

class ReferralsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.referrer = User.objects.create_user(username='referrer', password='test123')
        self.referred = User.objects.create_user(username='referred', password='test123')

    def test_referral_creation(self):
        # Log in the referrer
        self.client.login(username='referrer', password='test123')
        url = reverse('referral_list_create')  # from referrals/urls.py
        response = self.client.post(url, {'referred_user': self.referred.id})
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Referral.objects.filter(referrer=self.referrer, referred_user=self.referred).exists())
