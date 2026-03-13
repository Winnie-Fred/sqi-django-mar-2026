from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    is_nigerian = models.BooleanField(default=True)
    picture = models.ImageField(upload_to="author_pictures/", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

