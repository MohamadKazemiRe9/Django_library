from django.urls import path
from .views import BooksViewApi

app_name="api-books"

urlpatterns = [
    path("<int:pk>",BooksViewApi.as_view(),name="books_api"),
]
