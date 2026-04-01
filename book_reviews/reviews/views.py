from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Book, Review
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
    book = get_object_or_404(Book, pk=book_id)
    form = ReviewForm()
    already_reviewed = False
    if request.user.is_authenticated:
        already_reviewed = book.already_reviewed(request.user)

    if request.method == "POST":
        
        if not request.user.is_authenticated:
            messages.error(request, "You need to be logged in to leave a review")
            return redirect("users:login")

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.added_by = request.user
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

@login_required
def edit_review(request, review_pk):
    review = get_object_or_404(Review, id=review_pk)

    if request.user != review.added_by:
        messages.error(request, "You do not have permission to perform that action")
        return redirect("reviews:book_detail", book_id=review.book.id) 

    if not review.can_still_edit:
        messages.error(request, "You can no longer edit that review")
        return redirect("reviews:book_detail", book_id=review.book.id)

    form = ReviewForm(instance=review)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("reviews:book_detail", book_id=review.book.id)

    context = {
        "review": review,
        "form": form
    }
    return render(request, "reviews/edit-review.html", context)

@login_required
def confirm_delete(request, review_pk):
    review = get_object_or_404(Review, id=review_pk)

    if request.user != review.added_by:
        messages.error(request, "You do not have permission to perform that action")
        return redirect("reviews:book_detail", book_id=review.book.id) 

    return render(request, "reviews/confirm-delete.html", {"review": review})

@login_required
def delete_review(request, review_pk):
    review = get_object_or_404(Review, id=review_pk)

    if request.user != review.added_by:
        messages.error(request, "You do not have permission to perform that action")
        return redirect("reviews:book_detail", book_id=review.book.id) 


    if request.method == "POST":
        review.delete()
    
    return redirect("reviews:book_detail", book_id=review.book.pk)