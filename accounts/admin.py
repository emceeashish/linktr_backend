from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'referral_code', 'get_referred_by', 'get_referrals_count')
    search_fields = ('username', 'email')
    readonly_fields = ('referral_code',)  # referral_code is non-editable

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Referral Info', {'fields': ('referred_by',)}),  # Only allow editing of "referred_by"
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'referred_by'),
        }),
    )

    def get_referred_by(self, obj):
        return obj.referred_by.username if obj.referred_by else "-"
    get_referred_by.short_description = 'Referred By'

    def get_referrals_count(self, obj):
        return obj.referrals.count()
    get_referrals_count.short_description = 'Total Referrals'
