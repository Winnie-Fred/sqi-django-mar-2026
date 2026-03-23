from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path('', views.home, name='home'),
    path('books/all/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('create/book/', views.create_book_model_form_auto_render, name='create_book_model_form_auto_render'),
    path('create/book-manual/', views.create_book_manual_form_manual_render, name='create_book_manual_form_manual_render'),
    path('books/update/<int:book_pk>/', views.update_book_model_form, name='update_book_model_form'),
    path('books/update-manual/<int:book_pk>/', views.update_book_manual_form, name='update_book_manual_form'),
    path('books/confirm-delete/<int:book_id>/', views.confirm_delete, name='confirm_delete'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
] 