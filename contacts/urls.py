from django.urls import path
from . import views

# URLS PATTERNS
urlpatterns = [
    path('inquiry', views.inquiry, name="inquiry"),

] 
