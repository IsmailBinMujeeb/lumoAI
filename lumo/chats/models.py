from django.db import models
from django.contrib.auth.models import User


class chat(models.Model):

    title = models.CharField()
    user = models.ForeignKey(User, models.CASCADE, related_name="user")

    def __str__(self):
        return self.title


class message(models.Model):

    text = models.TextField()
    isPrompt = models.BooleanField(default=True)
    hasMermaid = models.BooleanField(default=False)
    mermaid = models.TextField(default="")
    chat = models.ForeignKey(chat, on_delete=models.CASCADE, related_name="message")

    def __str__(self):
        return self.text
