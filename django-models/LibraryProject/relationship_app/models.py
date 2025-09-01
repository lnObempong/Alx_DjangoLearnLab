from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    # Many books can be written by one author (ForeignKey = many-to-one)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',  # lets us do author.books.all()
    )

    def __str__(self):
        return f"{self.title} — {self.author.name}"


class Library(models.Model):
    name = models.CharField(max_length=255)
    # A library can have many books, and a book can live in many libraries
    books = models.ManyToManyField(
        Book,
        related_name='libraries',
        blank=True,  # allows a library to be created without any books yet
    )

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    # Exactly one librarian per library and vice versa (one-to-one)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name='librarian',  # lets us do library.librarian
    )

    def __str__(self):
        return f"{self.name} ({self.library.name})"
