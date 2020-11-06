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