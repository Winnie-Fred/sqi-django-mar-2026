from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello_page, name='hello_page'),
    path('second-view/', views.second_view, name='second_view')
]