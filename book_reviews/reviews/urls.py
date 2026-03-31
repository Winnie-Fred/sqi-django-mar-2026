from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = [
    path('', views.home, name="home"),
    path('books/all/', views.books, name="all_books"),
    path('book/<int:book_id>/', views.book_detail, name="book_detail"),
]