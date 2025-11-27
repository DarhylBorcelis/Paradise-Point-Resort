from django.contrib import admin
from .models import Visitors

class Visitors_Admin(admin.ModelAdmin):
    list_display = ('visitor_name', 
                    'visitor_email', 
                    'visitor_contact', 
                    'visitor_purpose', 
                    'visit_date', 
                    'visit_time',
                    'visit_created_at',
                    )


admin.site.register(Visitors)
