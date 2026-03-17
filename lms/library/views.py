from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .models import Book
from .forms import BookForm

# Create your views here.

def home(request):
    return render(request, "library/home.html")

def book_list(request):
    books = Book.objects.all()
    return render(request, "library/book-list.html", {"books": books})


# def book_detail(request, book_id):
#     try:
#         book = Book.objects.get(id=book_id)
#     except Book.DoesNotExist:
#         raise Http404("Book with that ID does not exist")
#     return render(request, "library/book-detail.html", {"book": book})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "library/book-detail.html", {"book": book})


def create_book_model_form_auto_render(request):
    print("request: ", request)
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        print("request.POST: ", request.POST)
        print("request.FILES: ", request.FILES)
        if form.is_valid():
            form.save()
            return redirect("library:book_list")
        
    # print("form: ", form)
    # print("ERRORS------------------------")
    # print(form.errors)
    context = {"form": form}
    return render(request, "library/create-book-model-form-auto-render.html", context)