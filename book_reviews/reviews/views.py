from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib import messages

from .models import Book
from .forms import ReviewForm

User = get_user_model()

# Create your views here.

def home(request):
    return render(request, "reviews/index.html")


def books(request):
    all_books = Book.objects.all()
    context = {
        "all_books": all_books
    }
    return render(request, "reviews/books.html", context)


def book_detail(request, book_id):
    book = Book.objects.get(id=2)

    book = get_object_or_404(Book, pk=book_id)
    form = ReviewForm()
    already_reviewed = False
    if request.user.is_authenticated:
        already_reviewed = book.already_reviewed(request.user)

    if request.method == "POST":
        

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.added_by = User.objects.get(id=1)
            try:
                review.full_clean()
            except ValidationError as e:
                for message in e.messages:
                    messages.error(request, message)
                    form.add_error(None, message)
            else:
                review.save()
                return redirect("reviews:book_detail", book_id=book_id)
            

    context = {"book": book, "form": form, "already_reviewed": already_reviewed}
    return render(request, "reviews/book-detail.html", context)