from django.db import models

from authors.models import Author

# Create your models here.
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=255)
    number_of_pages = models.PositiveIntegerField()
    published_on = models.DateField()
    cover_image = models.ImageField(upload_to="cover_images/", default="default_cover_image.jpg")

    def __str__(self):
        return f"{self.title} by {self.author}"