from django.contrib.auth.models import AbstractUser
from django.db import models

class Collaborateur(AbstractUser):
    ROLE_CHOICES = [
        ('commercial', 'Commercial'),
        ('support', 'Support'),
        ('gestion', 'Gestion'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
