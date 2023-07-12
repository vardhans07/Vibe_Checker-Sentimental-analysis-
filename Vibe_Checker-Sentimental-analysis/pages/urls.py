from django.urls import path
from pages.views import SentimentApp
from .import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
     path('/about/', SentimentApp, name='about'),
]
