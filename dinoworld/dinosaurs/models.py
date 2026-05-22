from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Dinosaur(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    image = models.URLField()

    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name