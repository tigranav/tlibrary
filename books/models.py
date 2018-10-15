from django.db import models
from django.utils import timezone

# Create your models here.

STORAGE_TYPE_CHOICES = (
    (2, "General"),
    (3, "Yandex"),
    (4, "Google"),
    (5, "RemoteStorage"),
    (1, "Unknown"),
)

COMPRESSOR_CHOICES = (
    (1, "Uncompressed"),
    (1, "7zip"),
    (3, "rar"),
    (4, "tgz"),
)

class Book(models.Model):
    old = models.BigIntegerField(help_text="old id")
    title = models.CharField(max_length=255, help_text="Title of books")
    author = models.CharField(max_length=255, help_text="authors")
    year = models.IntegerField(help_text="year")
    pages_count = models.IntegerField(help_text="number of pages", default=0)
    description = models.CharField(max_length=4000, help_text="Description")
    isbn = models.CharField(max_length=40, help_text="ISBN", default="")
    inserted = models.DateTimeField(default=timezone.now)

    # Metadata
    class Meta:
        ordering = ["title"]

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.title+" "+self.author


class BookItem(models.Model):
    book_id = models.ForeignKey('Book',on_delete=models.CASCADE,)
    file_format = models.CharField(max_length=10, help_text="Format of file pdf,djvu,doc,fb2...")
    file_size = models.IntegerField(help_text="Size of file in bytes")
    compressor = models.IntegerField(choices=COMPRESSOR_CHOICES, default=1, help_text="Compressor type")
    compressor_password = models.CharField(max_length=30, help_text="password on file")

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.file_format+" "+str(self.file_size)


class Storage(models.Model):
    name = models.CharField(max_length=10, help_text="Name of storage")
    type = models.IntegerField(choices=STORAGE_TYPE_CHOICES, default=1, help_text="Storage type")
    size = models.IntegerField(help_text="Size of storage in bytes", default=0)
    used = models.IntegerField(help_text="usage storage in bytes", default=0)
    available = models.BooleanField(help_text="status of avaliable",default=False)
    last_accessable = models.DateTimeField(help_text="Last used timestamp", default=None)

    def get_absolute_url(selfself):
        return reverse('book:detail', kwargs={'pk': self.pk})

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name + " ("+str(self.type)+")"


class BookItemPlace(models.Model):
    item_id = models.ForeignKey('BookItem',on_delete=models.CASCADE,)
    storage_id = models.ForeignKey('Storage',on_delete=models.CASCADE,)



