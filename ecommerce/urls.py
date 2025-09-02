from django.urls import path
from . import views

urlpatterns = [
    path('', views.ecommerce_view, name='ecommerce_home'),
]