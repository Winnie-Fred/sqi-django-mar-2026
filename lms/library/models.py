from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError

from authors.models import Author


def validate_title(value: str):
    if not value.startswith("The "):
        raise ValidationError("Title must start with 'The '")

# Create your models here.
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=255, validators=[validate_title])
    number_of_pages = models.PositiveIntegerField(validators=[MaxValueValidator(7000)])
    published_on = models.DateField()
    cover_image = models.ImageField(upload_to="cover_images/", default="default_cover_image.jpg")

    def __str__(self):
        return f"{self.title} by {self.author}"