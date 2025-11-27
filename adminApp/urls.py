from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('booking_management', views.booking_management, name='booking_management'),
    path('booking/edit/<int:id>/', views.edit_booking, name='edit_booking'),
    path('booking/delete/<int:id>/', views.delete_booking, name='delete_booking'),

    path('visit_reservation', views.visit_reservation, name="visit_reservation"),
    
    path('services', views.services_management, name="services_management"),
    path('services/edit/<int:id>/', views.edit_service, name='edit_service'),
    path('services/delete/<int:id>/', views.delete_service, name='delete_service'),

    path('canceled', views.canceled, name="canceled"),
    path('revenue', views.revenue, name="revenue"),



]