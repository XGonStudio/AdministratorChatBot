from django import forms
from .models import Event
from user.models import User


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['description', 'client_phone', 'worker']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['worker'].queryset = User.objects.filter(is_admin=False)