from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book

# Create your views here.

def home(request):
    return render(request, "library/home.html")

def book_list(request):
    return render(request, "library/book-list.html")


# def book_detail(request, book_id):
#     try:
#         book = Book.objects.get(id=book_id)
#     except Book.DoesNotExist:
#         raise Http404("Book with that ID does not exist")
#     return render(request, "library/book-detail.html", {"book": book})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "library/book-detail.html", {"book": book})
