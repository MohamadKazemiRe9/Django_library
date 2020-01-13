from django.urls import path
from . import views

app_name="books"

urlpatterns = [
    path("",views.booksInfo,name="booksInfo"),
    path("<int:book_id>/",views.details, name="details"),
    path('vote/<int:id>',views.vote,name="vote"),
]
