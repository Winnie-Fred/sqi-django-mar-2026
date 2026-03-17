from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path('', views.home, name='home'),
    path('books/all/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('create/book/', views.create_book_model_form_auto_render, name='create_book_model_form_auto_render'),
] 