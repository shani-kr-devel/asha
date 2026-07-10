from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('epower/<int:pk>/', views.epower_detail, name='epower_detail'),
]
