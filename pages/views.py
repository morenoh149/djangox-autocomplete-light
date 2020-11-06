from django.views.generic import TemplateView
from .forms import CompanyForm
from .models import Company
from dal import autocomplete
from django.db.models import Q

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
            qs = qs.filter(Q(ticker__icontains=self.q) | Q(name__icontains=self.q))

        return qs