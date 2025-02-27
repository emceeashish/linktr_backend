from django.db import models
from django.conf import settings

class Referral(models.Model):
    referrer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='outgoing_referrals'
    )
    referred_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='incoming_referral'
    )
    referred_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referrer.username} -> {self.referred_user.username}"
