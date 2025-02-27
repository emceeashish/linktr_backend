from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Welcome to the Linktr Backend API!"})

urlpatterns = [
    path('', home_view, name='home'),  # A simple JSON homepage
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/referrals/', include('referrals.urls')),
]
