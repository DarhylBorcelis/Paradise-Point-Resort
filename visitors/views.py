from django.shortcuts import render
from django.contrib import messages
from .models import Visitors

# Create your views here.
def visitors_index(request):

    if request.method == 'POST':
        visitor_name = request.POST.get('name')
        visitor_email = request.POST.get('email')
        visitor_contact = request.POST.get('contact')
        visitor_purpose = request.POST.get('purpose')
        visit_date = request.POST.get('visit_date')
        visit_time = request.POST.get('visit_time')


        try:
            Visitors.objects.create(
                visitor_name=visitor_name,
                visitor_email=visitor_email,
                visitor_contact=visitor_contact,
                visitor_purpose=visitor_purpose,
                visit_date=visit_date,
                visit_time=visit_time,
            )
            messages.success(request, "Visitor request submitted successfully!")
        except Exception as e:
            messages.error(request, "Error submitting visitor request")

    return render(request, 'visitors_html/visitors_index.html')