from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('',views.index, name="index" ),
        path('submit-valunteer',views.submit_valunteer, name="submit-valunteer" ),
        path('contact',views.contact, name="contact" ),
        path('donate/<int:id>',views.donate, name="donate" ),
]
