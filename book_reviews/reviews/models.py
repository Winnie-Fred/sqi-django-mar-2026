import datetime

from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    year_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class GenreChoices(models.TextChoices):
    FANTASY = "FTSY", "Fantasy"
    SCI_FI = "SCIFI", "Science Fiction"
    MYSTERY_THRILLER = "MYST_THRILL", "Mystery/Thriller"
    ROMANCE = "ROM", "Romance" 
    HISTORICAL_FICTION = "HIST_FIC", "Historical Fiction"
    HORROR = "HORROR", "Horror"
    DYSTOPIAN = "DYST", "Dystopian"
    ADVENTURE = "ADVN", "Adventure"
    BIO_AUTOBIO = "BIO_AUTOBIO", "Biography/Autobiography"
    SELF_HELP = "SELF_HELP", "Self Help"
    HISTORY = "HIST", "History"
    SCIENCE = "SCI", "Science"
    BUSINESS = "BSNS", "Business"

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genre = models.CharField(choices=GenreChoices.choices, default=GenreChoices.FANTASY, max_length=11)
    publication_date = models.DateField()
    isbn = models.CharField()
    number_of_pages = models.IntegerField()
    cover_image = models.ImageField(upload_to="book_cover_images/")

    def already_reviewed(self, added_by):
        return self.reviews.filter(added_by=added_by).exists()

    def average_rating(self):
        all_ratings = [rating_dict["rating"] for rating_dict in self.reviews.values("rating")]
        return sum(all_ratings) / len(all_ratings) if all_ratings else 0
        
    def float_average_rating(self):
        return round(self.average_rating(), 1)
    
    def int_average_rating(self):
        return round(self.average_rating())

    def __str__(self):
        return f"{self.title} by {self.author}"


class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_reviews")
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.added_by} on {self.book.title} - {self.rating} stars: {self.content[:100]}..."

    def clean(self):
        # Don't allow user to leave more than one review
        if not self.pk and getattr(self, "book", None) and self.book.already_reviewed(self.added_by):
            print(f"Calling .clean() -> {getattr(self, "book", None)} and {self.book.already_reviewed(self.added_by)}")
            raise ValidationError("You have already reviewed this book. You can try editing your existing review.")
        super().clean()

    @property
    def can_edit_for(self):
        can_edit_until = self.added_at + datetime.timedelta(minutes=5)
        if can_edit_until < timezone.now():
            return 0
        return (can_edit_until - timezone.now()).seconds

    @property
    def can_still_edit(self):
        return self.can_edit_for != 0
