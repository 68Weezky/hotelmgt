from django.shortcuts import render, redirect
from .models import Event
from .forms import EventBookingForm
from django.contrib import messages
from django.utils import timezone

# Create your views here.

def events_index(request):
    now = timezone.now().date()
    events = Event.objects.all().order_by('date', 'time')
    upcoming_events = events.filter(date__gte=now)
    past_events = events.filter(date__lt=now)
    form = EventBookingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Your RSVP was successful!')
        return redirect('events_index')
    return render(request, 'events_index.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'form': form
    })
