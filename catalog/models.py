from django.db import models


class Genre(models.Model):
    """Model representing a book genre"""

    name = models.CharField(
        max_length=200, help_text="Enter a book genre (e.g. Science Fiction)"
    )

    def __str__(self):
        """String representation of the Genre object"""
        return self.name
