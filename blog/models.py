from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# each class will create table and its attribute will become tables field
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title