from django.urls import path
from . import views


urlpatterns = [
    path('', views.visitors_index, name='visitors_index')
]