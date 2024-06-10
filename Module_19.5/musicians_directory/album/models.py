from django.db import models

from musician.models import Musician


class Album(models.Model):
    name = models.CharField(max_length=255)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField(auto_now_add=True)
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    ratings = models.CharField(max_length=1, choices=RATING_CHOICES)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.musician.full_name}"