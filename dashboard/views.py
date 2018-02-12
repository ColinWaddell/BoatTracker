from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from log.models import Reading


def index(request, reading_id=None):
    if reading_id:
        reading = get_object_or_404(Reading, pk=reading_id)
    else:
        reading = Reading.objects.last()

    return render(
            request,
            'dashboard.html',
            {
                "readings": Reading.objects.all(),
                "requested_reading": reading,
            }
        )
