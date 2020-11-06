from django.views.generic import TemplateView
from accounts.forms import PersonForm

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self):
        return {"form": PersonForm()}


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'