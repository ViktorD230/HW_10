from django.db import models

# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=25, null=False, unique=True)
    born_date = models.CharField(max_length=25, null=True)
    born_location = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.fullname}"
    
class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Quote(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.TextField()

    def __str__(self):
        return f"{self.quote}"
    