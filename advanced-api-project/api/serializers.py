from.models import Book, Author  # Ensure models are correctly imported
from restframework import serializers
from.serializers import BookSerializer  #assuming serializers is in the same field
from.datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'  #Return all the fields

    def validate_date(self, values):  #This method is automatically calls the serializer validation for the publication_year field
        current_year = date.today().year
        if value >current_year:
            raise serializers.ValidationError("The year does notexist")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True, source='book_set') #Nested books

    class Meta: 
        model = Author
        fields = ['name'] #Returns only the name field
