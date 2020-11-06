from django.views.generic import TemplateView
from .forms import CompanyForm
from .models import Company
from dal import autocomplete


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self):
        return {"company_form": CompanyForm()}


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class CompanyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Company.objects.all()

        if self.q:
            qs = qs.filter(email__istartswith=self.q)

        return qs