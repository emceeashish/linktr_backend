from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    referral_code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    referred_by = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='referrals'
    )

    def __str__(self):
        return self.username
