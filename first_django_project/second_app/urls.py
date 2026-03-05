from django.urls import path

from . import views

urlpatterns = [
    path('second-app-view/', views.second_app_view, name='second_app_view'),
]