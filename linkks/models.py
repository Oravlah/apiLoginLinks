from django.db import models
from users.models import User
# Create your models here.


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links')
    url = models.URLField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.url}"
