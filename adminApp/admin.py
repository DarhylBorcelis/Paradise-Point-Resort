from django.contrib import admin
from .models import Services, Booking


class Services_Admin(admin.ModelAdmin):
    list_display = ( 'service_name',
                     'service_price'
                    )

# Register your models here.
admin.site.register(Services)
admin.site.register(Booking)
