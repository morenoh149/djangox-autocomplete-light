from django.shortcuts import render

from dal import autocomplete

from .models import CustomUser


class CustomUserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = CustomUser.objects.all()

        if self.q:
            qs = qs.filter(email__istartswith=self.q)

        return qs