from django.db import models


class Author(models.Model):
    full_name = models.TextField(max_length=50)
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.CharField(max_length=128)
    description = models.TextField()
    year_release = models.SmallIntegerField()
    authors = models.ManyToManyField(
        Author,
        through='Inspiration',
        through_fields=('book', 'author')
    )
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    redaction = models.ForeignKey('Redaction', on_delete=models.CASCADE, null=True, blank=True, related_name='books')

    def __str__(self):
        return self.title


class Inspiration(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    inspirer = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='inspired_works',
    )

    def __str__(self):
        return f'{self.book} - {self.author} - {self.inspirer}'


class Redaction(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
