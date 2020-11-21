from django.db import models

# Create your models here.


class Genre(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag')
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    date_of_birth = models.DateField(
        blank=False, auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Tag(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title

