from django import forms
from .models import Company
from dal import autocomplete


class TickerWidget(autocomplete.ListSelect2):
    autocomplete_function = "ticker_autocomplete_init"


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["ticker"]
        widgets = {
            "ticker": TickerWidget(
                url="company-autocomplete",
                attrs={
                    "data-ajax-delay": "250",
                    "data-tags": "true",
                },
            )
        }