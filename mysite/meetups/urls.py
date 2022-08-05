from django.urls import path

from . import views

urlpatterns = [
    path('peeps/', views.index), # our-domain.com/meetups
    path('greet/', views.greetings)
]

 