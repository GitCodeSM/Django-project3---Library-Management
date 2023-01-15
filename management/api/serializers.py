# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from management.models import Book,Member

class BookSerializer(serializers.ModelSerializer):
    # book_cover = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Book
        fields = "__all__"
        
class MemberSerializer(serializers.ModelSerializer):
    #related name i.e mybooks #nested relationship between two model serializers
    mybooks = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Member
        fields = "__all__"