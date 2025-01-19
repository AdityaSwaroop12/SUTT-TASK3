from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    total_copies = models.PositiveIntegerField()
    borrowed_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='book_covers/',default='book_covers/default_cover.jpg')

    def __str__(self):
        return self.title

class UploadedFile(models.Model):
    file = models.FileField(upload_to='media/uploaded_excels/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default = 1)
    name = models.CharField(max_length=100)
    psrn = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name

class UserProfile1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default = 1)
    name = models.CharField(max_length=100)
    hostel = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    branch = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name
