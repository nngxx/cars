from django.urls import path
from car import views

urlpatterns = [
    path('get-cars/', views.CarView.as_view()),
]
