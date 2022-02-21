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
    path('milwaukee/', views.mil, name='mil'),
    path('newyork/', views.nyc, name='nyc'),
    path('orlando/', views.orl, name='orl'),
    path('philadelphia/', views.phi, name='phi'),
    path('toronto/', views.tor, name='tor'),
    path('washington/', views.was, name='was'),
    path('dallas/', views.dal, name='dal'),
    path('denver/', views.den, name='den'),
]