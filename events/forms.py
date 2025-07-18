from django import forms
from .models import EventBooking, Event

class EventBookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        fields = ['event', 'attendee_name', 'attendee_email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event'].queryset = Event.objects.all().order_by('date', 'time') 