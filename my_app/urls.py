from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('covered_loads/', views.covered, name="covered")
]