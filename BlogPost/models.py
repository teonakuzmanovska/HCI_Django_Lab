from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Publication(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.TextField(null=True, blank=True)
    files = models.FileField(null=True, blank=True)
    creation_date = models.DateField(auto_now=True,)
    last_modified = models.DateTimeField(auto_now=True,)


class Comment(models.Model):
    comment = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CommentOnPublication(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class BlockedUsers(models.Model):
    blocked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blocked_user")
    blocker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blocker")


