from django.shortcuts import render, get_object_or_404, redirect

from .models import Book
from reviews.forms import ReviewForm

# Create your views here.
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    review_form = ReviewForm()
    
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.book = book
            review.save()
            return redirect("books:book_detail", book_id=book_id)
    
    context = {
        "book": book,
        "form": review_form
    }
    return render(request, "books/book-detail.html", context)