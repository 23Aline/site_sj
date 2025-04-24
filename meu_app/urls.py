from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vinicolas/', views.vinicolas, name='vinicolas'),
    path('destaques/', views.destaques, name='destaques'),
    path('clima/', views.clima, name='clima'),
    path('video/', views.video, name='video'),
]
