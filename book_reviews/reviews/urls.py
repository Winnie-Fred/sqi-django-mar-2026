from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = [
    path('', views.home, name="home"),
    path('books/all/', views.books, name="all_books"),
    path('book/<int:book_id>/', views.book_detail, name="book_detail"),
    path('edit/review/<int:review_pk>/', views.edit_review, name="edit_review"),
    path('confirm/delete/<int:review_pk>/', views.confirm_delete, name="confirm_delete"),
    path('delete/review/<int:review_pk>/', views.delete_review, name="delete_review"),
]