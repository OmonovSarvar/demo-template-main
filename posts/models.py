from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class chat(models.Model):
    full_name = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=40)
    post_content = models.CharField(max_length=240)
    post_date = models.DateTimeField(default=timezone.datetime.now)

    def __str__(self):
        return f"Post {self.full_name} tomonidan yozildi!"
