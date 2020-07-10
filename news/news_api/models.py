from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(
                    Post,
                    related_name="comments",
                    on_delete=models.CASCADE)

    def __str__(self):
        return self.author_name
