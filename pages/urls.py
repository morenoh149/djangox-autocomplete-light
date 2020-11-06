from django.urls import path

from .views import CompanyAutocomplete, HomePageView, AboutPageView
from accounts.views import CustomUserAutocomplete

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path(
        'custom-user-autocomplete/',
        CustomUserAutocomplete.as_view(),
        name='custom-user-autocomplete',
    ),
    path(
        'company-autocomplete/',
        CompanyAutocomplete.as_view(),
        name='company-autocomplete',
    ),
]
