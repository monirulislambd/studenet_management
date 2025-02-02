from django.db import models
import os


def create_directory(instance, filename):
    return os.path.join('student/media/' , instance.name, filename)
# Create your views here.

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=11, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    photo = models.ImageField(upload_to= create_directory, blank=False, null=False)
    checkbox = models.BooleanField(blank=True)
    def __str__(self):
        return f"{self.name}" 