from django.db import models
from django.utils import timezone

# Create your models here.
class Visitors(models.Model):
    visitor_name = models.CharField(max_length=100)
    visitor_email = models.EmailField(max_length=50, blank=True, null=True)
    visitor_contact = models.CharField(max_length=50)
    visitor_purpose = models.CharField(max_length=50, blank=True)
    visit_date = models.DateField()
    visit_time = models.TimeField(null=True, blank=True)
    visit_created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.visitor_name