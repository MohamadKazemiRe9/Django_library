from rest_framework import generics
from books.models import Books
from django.shortcuts import get_list_or_404,get_object_or_404
from .serializers import BooksSerializer

class BooksViewApi(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    serializer_class = BooksSerializer

    def get_queryset(self):
        return Books.objects.all()

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Books,pk = pk)