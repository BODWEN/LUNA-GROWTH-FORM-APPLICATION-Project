from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('applicant/', views.applicant, name='applicant'),
    path('guarantor/', views.guarantor, name='guarantor'),
]