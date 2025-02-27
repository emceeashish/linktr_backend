from rest_framework import serializers
from .models import Referral

class ReferralSerializer(serializers.ModelSerializer):
    referrer_username = serializers.ReadOnlyField(source='referrer.username')
    referred_username = serializers.ReadOnlyField(source='referred_user.username')

    class Meta:
        model = Referral
        fields = [
            'id',
            'referrer', 'referrer_username',
            'referred_user', 'referred_username',
            'referred_at',
        ]
        read_only_fields = ['id', 'referrer', 'referred_at']
