from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    faculty = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'faculty'})

    def __str__(self):
        return self.title

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.course.title})"

