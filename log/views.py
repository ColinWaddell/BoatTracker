from json import dumps

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Reading


def update(request, latitude, longitude, battery_v, pumping):

    feedback = {"error": ""}

    try:
        logged_reading = Reading(
            latitude=float(latitude),
            longitude=float(longitude),
            battery_v=float(battery_v),
            pumping=float(pumping),
            datetime=timezone.now()
        )
        logged_reading.save()

    except Exception as e:
        feedback = {
            "error": str(e)
        }

    finally:
        return HttpResponse(dumps(feedback))
