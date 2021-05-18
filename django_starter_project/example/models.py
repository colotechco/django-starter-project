from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    title = models.CharField('Title', max_length=100, unique=True)
    description = models.TextField('Description')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    due = models.DateTimeField('Due')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
