from django.db import models

# Create your models here.
class Services(models.Model):
    service_name = models.CharField(max_length=50)
    service_description = models.TextField(max_length=200)
    service_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name
    
class Booking(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CHECKED_IN', 'Checked-In'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
        ('NO_SHOW', 'No-Show'),
    ]

    PAYMENT_METHODS = [
        ('CASH', 'Cash'),
        ('GCASH', 'GCash'),
        ('BANK', 'Bank Transfer'),
    ]

    services = models.ManyToManyField('Services', blank=True)


    fullname = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    email = models.EmailField()
    checkIn_date = models.DateField()
    checkOut_date = models.DateField()
    number_of_guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='CASH')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.status}"


    
