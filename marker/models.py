from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, blank=True )
    published_date = models.DateField()
    genre = models.ManyToManyField(Genre, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    summary = models.TextField()

    def __str__(self):
        authors = ", ".join([str(a) for a in self.author.all()])
        genres = ", ".join([str(g) for g in self.genre.all()])
        company = self.company.name if self.company else "Unknown"
        return f"{self.title} by {authors} in {company}, genre: {genres} (added {self.published_date})"
class Impression(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Impression for {self.book.title} at {self.created_at}"

