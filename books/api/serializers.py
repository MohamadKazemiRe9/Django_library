from rest_framework import serializers
from books.models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        # fields = [
        #     'pk',
        #     'name',
        #     'auther',
        # ]
        fields ="__all__"
        read_only_fields = ["pk"]
