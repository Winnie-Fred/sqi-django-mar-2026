from django.contrib.auth import get_user_model

from library.models import Book

User = get_user_model()

first_user = User.objects.get(pk=1)

all_books = Book.objects.all()

for book in all_books:
    book.added_by = first_user
    book.save()

