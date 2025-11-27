from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Services
from visitors.models import Visitors

# Create your views here.
def dashboard(request):
    all_booking = Booking.objects.all()
    return render(request, 'admin_html/dashboard.html', {'bookings': all_booking})

def booking_management(request):
    all_booking = Booking.objects.all()
    return render(request, 'admin_html/booking_management.html', {'bookings':all_booking})

def edit_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    services = Services.objects.all()

    if request.method == "POST":
        booking.fullname = request.POST.get('fullname')
        booking.contact = request.POST.get('contact')
        booking.email = request.POST.get('email')
        booking.checkIn_date = request.POST.get('checkIn_date')
        booking.checkOut_date = request.POST.get('checkOut_date')
        booking.total_price = request.POST.get('total_price')
        booking.payment_method = request.POST.get('payment_method')
        booking.status = request.POST.get('status')

        selected_services = request.POST.getlist('services')
        booking.services.set(selected_services)

        booking.save()
        return redirect('booking_management')

    return render(request, 'admin_html/edit_booking.html', {
        'booking': booking,
        'services': services
    })

def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.delete()

    return redirect('booking_management')


def visit_reservation(request):
    all_visitors = Visitors.objects.all()
    return render(request, 'admin_html/visit_reservation.html', {'visitors':all_visitors})

def services_management(request):
    all_services = Services.objects.all()
    if request.method == "POST":
        service_name = request.POST.get('service_name')
        description = request.POST.get('service_description')
        service_price = request.POST.get('service_price')

        Services.objects.create(
            service_name=service_name,
            service_description=description,
            service_price=service_price
        )
        
    return render(request, 'admin_html/services_management.html', {'services': all_services})

def edit_service(request, id):
    service = Services.objects.get(id=id)

    if request.method == "POST":
        service.service_name = request.POST.get("service_name")
        service.service_description = request.POST.get("service_description")
        service.service_price = request.POST.get("service_price")
        service.save()

        return redirect('services_management')

    return render(request, 'admin_html/edit_service.html', {"service": service})

def delete_service(request, id):
    service = Services.objects.get(id=id)
    service.delete()
    return redirect('services_management')

def canceled(request):
    return render(request, 'admin_html/canceled.html')

def revenue(request):
    return render(request, 'admin_html/revenue.html')


