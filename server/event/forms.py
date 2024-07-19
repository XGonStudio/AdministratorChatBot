from django import forms
from .models import Event
from user.models import User


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'description', 'client_phone', 'worker']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control datepicker'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'client_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter client phone number'}),
            'worker': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['worker'].queryset = User.objects.filter(is_admin=False)