from django.contrib import admin

# Register your models here.

from .models import Student

admin.site.register(Student)  # Registering Book model in Django admin panel.  # noqa: E501

# This will allow you to see and edit the Book objects in the Django admin site.  # noqa: E501
