from django.urls import path

from letter import views

app_name = 'letter'

urlpatterns = [
    path('', views.give_letter, name='give_letter')
]