from django.urls import path
from . import views

urlpatterns = [
    path('', views.service),
    path('web/', views.web),
    path('app/', views.app),
    path('seo/', views.seo),
    
]