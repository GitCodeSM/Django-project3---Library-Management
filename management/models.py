from django.db import models

# Create your models here.

class Member(models.Model):

    member_name = models.CharField(max_length=100)

class Book(models.Model):
    book_title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    book_cover = models.ImageField(upload_to='static/')
    description = models.TextField()
    status = models.CharField(default="Available", max_length=10)
    member_name = models.ForeignKey(Member, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
	    return self.book_title
