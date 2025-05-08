from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    health = models.IntegerField(default=100)
    location = models.CharField(max_length=100, default="Atlantis Gate")
    inventory = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Narrative(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField()
    choices = models.JSONField()

    def __str__(self):
        return self.location
