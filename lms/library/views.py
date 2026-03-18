from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .models import Book
from .forms import BookForm, BookManualForm

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


def create_book_manual_form_manual_render(request):
    form = BookManualForm()
    if request.method == "POST":
        form = BookManualForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # Book.objects.create(
            #     title=cleaned_data['title'],
            #     author=cleaned_data['author'],
            #     number_of_pages=cleaned_data['number_of_pages'],
            #     published_on=cleaned_data['published_on'],
            #     cover_image=cleaned_data['cover_image']
            # )
            # print("cleaned data cover image: ", cleaned_data["cover_image"])
            # cover_image = cleaned_data.pop('cover_image')
            # print("popped cover image: ", cover_image)
            # book = Book(**cleaned_data)
            # if cover_image:
            #     book.cover_image = cover_image
            # print("book: ", book)
            # book.save()
            # Book.objects.create(**cleaned_data)
            book = Book.objects.create(
                title=cleaned_data['title'],
                author=cleaned_data['author'],
                number_of_pages=cleaned_data['number_of_pages'],
                published_on=cleaned_data['published_on'],
            )
            if cleaned_data["cover_image"]:
                book.cover_image = cleaned_data["cover_image"]
                book.save()

            return redirect("library:book_list")
        
    context = {"form": form}
    return render(request, "library/create-book-manual-form-manual-render.html", context)


