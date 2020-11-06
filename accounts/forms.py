from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from dal import autocomplete

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)

class PersonForm(forms.ModelForm):
    email = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        widget=autocomplete.ModelSelect2(url='custom-user-autocomplete')
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'username')

class TickerWidget(autocomplete.ListSelect2):
    autocomplete_function = "ticker_autocomplete_init"


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email"]
        widgets = {
            "email": TickerWidget(
                url="custom-user-autocomplete",
                attrs={
                    "data-ajax-delay": "250",
                    "required": True,
                    "data-tags": "true",
                },
            )
        }