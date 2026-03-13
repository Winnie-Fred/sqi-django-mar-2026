from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Author
from library.models import Book

# Create your views here.

def all_authors(request):
    return render(request, "authors/authors.html")

def book_signings(request):
    return render(request, "authors/book-signings.html")

def full_mvt(request):
    try:
        non_existent_author = Author.objects.get(pk=7)
    except Author.DoesNotExist:
        non_existent_author = None

    context = {
        'all_authors': Author.objects.all(),
        'non_nigerians': Author.objects.filter(is_nigerian=False),
        'nigerians': Author.objects.exclude(is_nigerian=False),
        # 'born_before_1975': Author.objects.filter(birth_date__lt=datetime(1975, 1, 1)),
        'born_before_1975': Author.objects.filter(birth_date__year__lt=1975),
        'non_existent_author': non_existent_author,
        # 'non_existent_author': get_object_or_404(Author, pk=1000),
        'authors_in_asc_order_of_birth': Author.objects.order_by('birth_date'),
        'authors_in_desc_order_of_birth': Author.objects.order_by('-birth_date'),
        'first_5_authors_asc': Author.objects.order_by('birth_date')[:5],
    }
    return render(request, "authors/full-mvt.html", context)

# 1. Get all the books
# 2. Get all the books published after 2nd of Feb, 1997
# 3. Get all the books in desc order (title)