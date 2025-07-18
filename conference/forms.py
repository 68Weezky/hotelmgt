from django import forms
from .models import ConferenceBooking, ConferenceRoom

class ConferenceBookingForm(forms.ModelForm):
    class Meta:
        model = ConferenceBooking
        fields = ['conference_room', 'booker_name', 'booker_email', 'date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['conference_room'].queryset = ConferenceRoom.objects.all()
        if self.fields['conference_room'].queryset.count() == 1:
            self.fields['conference_room'].initial = self.fields['conference_room'].queryset.first()
            self.fields['conference_room'].widget = forms.HiddenInput() 