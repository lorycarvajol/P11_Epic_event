from django import forms
from .models import Collaborateur

class CollaborateurForm(forms.ModelForm):
    class Meta:
        model = Collaborateur
        fields = ['username', 'email', 'role', 'password', 'is_active']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super(CollaborateurForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
