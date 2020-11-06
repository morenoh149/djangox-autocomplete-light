from django.urls import path

from .views import CompanyAutocomplete, HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path(
        'company-autocomplete/',
        CompanyAutocomplete.as_view(),
        name='company-autocomplete',
    ),
]
