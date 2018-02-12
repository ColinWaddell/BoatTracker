from django.contrib import admin
from .models import Reading


class ReadingAdmin(admin.ModelAdmin):
    model = Reading
    list_display = (
        'datetime',
        'latitude',
        'longitude',
        'battery_v',
        'pumping',
    )

admin.site.register(Reading, ReadingAdmin)
