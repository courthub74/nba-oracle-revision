from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atlanta/', views.atl, name='atl'),
    path('boston/', views.bos, name='bos'),
    path('brooklyn/', views.bklyn, name='bklyn'),
    path('charlotte/', views.char, name='char'),
    path('chicago/', views.chi, name='chi'),
    path('cleveland/', views.cle, name='cle'),
    path('detroit/', views.det, name='det'),
    path('indiana/', views.ind, name='ind'),
    path('miami/', views.mia, name='mia'),
]