from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atlantahawks/', views.atl, name='atl'),
    path('bostonceltics/', views.bos, name='bos'),
    path('brooklynnets/', views.bklyn, name='bklyn'),
    path('charlottehornets/', views.char, name='char'),
    path('chicagobulls/', views.chi, name='chi'),
    path('clevelandcavaliers/', views.cle, name='cle'),
    path('detroitpistons/', views.det, name='det'),
    path('indianapacers/', views.ind, name='ind'),
    path('miamiheat/', views.mia, name='mia'),
    path('milwaukeebucks/', views.mil, name='mil'),
    path('newyorkknicks/', views.nyc, name='nyc'),
    path('orlandomagic/', views.orl, name='orl'),
    path('philadelphia76ers/', views.phi, name='phi'),
    path('torontoraptors/', views.tor, name='tor'),
    path('washingtonwizards/', views.was, name='was'),
    path('dallasmavericks/', views.dal, name='dal'),
    path('denvernuggets/', views.den, name='den'),
    path('goldenstatewarriors/', views.gsw, name='gsw'),
]