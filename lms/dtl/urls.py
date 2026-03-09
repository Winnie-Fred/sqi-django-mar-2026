from django.urls import path

from . import views

urlpatterns = [
    path('', views.dtl_syntax_demo, name='dtl'),
]