from django.urls import path
from appIngles import views

urlpatterns = [
    path('',views.index),
    path('/courses/',views.courses),
    path('/team/',views.team),
    path('/in_companyTraining/',views.in_companyTraining),
]

 