from django.db import models

# Create your models here.

class Book(models.Model):
    old_id = models.BigIntegerField(help_text="old id")
    title = models.CharField(max_length=255, help_text="Title of books")
    author = models.CharField(max_length=255, help_text="authors")
    year = models.IntegerField(help_text="year")
    pages = models.IntegerField(help_text="number of pages")
    description = models.CharField(max_length=4000, help_text="Description")
    ISBN = models.CharField(max_length=40, help_text="ISBN")
    inserted = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ["title"]

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.title+" "+self.author

