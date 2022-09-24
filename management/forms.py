
from django import forms
from .models import Book

# Create your forms here.
class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('book_title', 'author', 'book_cover', 'description', 'status', 'member_name')
