from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import timedelta

from adminApp.models import Services, Booking

# Create your views here.
def homePage_index(request):
    all_services = Services.objects.all()
    return render(request, 'html/homePage.html', {'services':all_services})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        repeat_pass = request.POST.get('repeat_pass')

        if repeat_pass == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist')
                return redirect('register')
            else:
                User.objects.create_user(username=username,email=email,password=password)
                return redirect('logIn')
        else:
            messages.info(request, 'Password not the same')

    return render(request, 'html/register.html')

def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credential invalid!')
    
    return render(request, 'html/logIn.html')

def logOut(request):
    auth.logout(request)
    return redirect('/')

def booking_form(request):
    services = Services.objects.all()
    bookings = Booking.objects.all()

    booked_dates = []
    for b in bookings:
        current_date = b.checkIn_date
        while current_date <= b.checkOut_date:
            booked_dates.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)

    if request.method == "POST":
        booking = Booking.objects.create(
            fullname=request.POST.get('fullname'),
            contact=request.POST.get('contact'),
            email=request.POST.get('email'),
            checkIn_date=request.POST.get('checkIn_date'),
            checkOut_date=request.POST.get('checkOut_date'),
            number_of_guests=request.POST.get('number_of_guests'),
            total_price=request.POST.get('total_price'),
            payment_method=request.POST.get('payment_method'),
        )

        selected_services = request.POST.getlist("services")
        booking.services.set(selected_services)

    return render(request, "html/booking_form.html", {"services": services,"booked_dates": booked_dates})

def  setting(request):
    return render(request, 'html/setting.html')



