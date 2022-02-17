from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atlanta/', views.atl, name='atl'),
    path('boston/', views.bos, name='bos'),
]