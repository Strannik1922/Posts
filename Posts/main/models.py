from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Posts(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    text = models.TextField()
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
