from django.contrib import admin
from .models import Referral

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('id', 'referrer', 'referred_user', 'referred_at')
    search_fields = ('referrer__username', 'referred_user__username')
