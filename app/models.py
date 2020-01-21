from django.db import models
from django.contrib.auth.models import User


class Prompt(models.Model):
    text = models.TextField()
    score = models.IntegerField(default=0)  # for +1-ing good prompts
    owner = models.ForeignKey(
        User, related_name="prompt", on_delete=models.CASCADE, null=True
    )


class Answer(models.Model):
    text = models.TextField()
    votes = models.IntegerField(default=0)
    owner = models.ForeignKey(
        User, related_name="answer", on_delete=models.CASCADE, null=True
    )
