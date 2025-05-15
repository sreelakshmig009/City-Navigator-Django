from django.db import models
from django.contrib.auth.models import User

class Map(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='maps')
    layout = models.JSONField()
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Coordinates validation used in path finding algorithm in views.py
    def is_valid_position(self, row, col):
        return 0 <= row < len(self.layout) and 0 <= col < len(self.layout[0])

    class Meta:
        ordering = ['-updated_at']