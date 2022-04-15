import uuid
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """Model representing a book genre"""

    name = models.CharField(
        max_length=200, help_text="Enter a book genre (e.g. Science Fiction)"
    )

    def __str__(self):
        """String representation of the Genre object"""
        return self.name


class Book(models.Model):
    """Model representing a single Book (not a specific copy)"""

    title = models.CharField(max_length=200)

    # using a Foreign key because the book can can only have one author,
    # but authors can have multiple books
    # # Author as a string rather that a model because it hasn't been declared yet in the file
    author = models.ForeignKey("Author", null=True, on_delete=models.SET_NULL)
    summary = models.TextField(
        blank=True, max_length=1000, help_text="Enter a brief description of the book"
    )
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        unique=True,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
    )

    # ManyToManyField used because a genre can contain many books. And books can cover many genres.
    # Genre class has already been defined so we can specify the class above
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    def __str__(self):
        """String representing the Book object"""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access the detail of the record."""
        return reverse("book-detail", args=[str(self.id)])


class BookInstance(models.Model):
    """A model representing a specific copy of a book (i.e. that can be borrowed from the library)"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular book in the whole library",
    )
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book Availability",
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """String representation of the Book instance"""
        return f"{self.id} ({self.book.title})"


class Author(models.Model):
    """A model representing a book Author"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse("author-detail", args=(str(self.id)))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
