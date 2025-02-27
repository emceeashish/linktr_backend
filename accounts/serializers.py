from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )
    referred_by_code = serializers.UUIDField(
        write_only=True,
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'referred_by_code']

    def create(self, validated_data):
        referred_by_code = validated_data.pop('referred_by_code', None)
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])

        # If there's a referral code, link the new user to the referrer
        if referred_by_code:
            try:
                referrer = User.objects.get(referral_code=referred_by_code)
                user.referred_by = referrer
            except User.DoesNotExist:
                pass

        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'referral_code', 'referred_by']
        read_only_fields = ['referral_code', 'referred_by']
