from django.urls import path

from . import views

urlpatterns = [
    path('meetups/', views.index), # our-domain.com/meetups
    path('greet/', views.greetings),
    path('meetups/<slug:meetup_slug>', views.meetup_details)
]

 