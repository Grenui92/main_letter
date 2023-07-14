from django.urls import path

from letter import views

app_name = 'letter'

urlpatterns = [
    path('', views.MainLetterView.as_view(), name='give_letter')
]