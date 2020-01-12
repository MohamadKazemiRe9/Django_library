from django.shortcuts import render , get_object_or_404 , get_list_or_404
from django.http import HttpResponse ,response,Http404
from .models import Books
from django.views import generic


def booksInfo(request):
    sort = get_list_or_404(Books.objects.order_by('name'))
    context = {"hot_books":sort}
    return render(request,"books/index.html",context)

# class IndexView(generic.ListView):
#     model = Books
#     template_name = "books/index.html"

#     def get_queryset(self):
#         return Books.objects.order_by('name')


def details(request,book_id):
    book_details = get_object_or_404(Books,id = book_id)
    return render(request,"books/details.html",{"book":book_details})

def vote(request,id):
    book = get_object_or_404(Books,pk = id)
    book.vote_number += 1
    if(book.vote_number == 1):
        book.vote += int(request.POST["vote"])
    else:
        book.vote = round(float((book.vote*(book.vote_number-1)) + float(request.POST["vote"]))/(book.vote_number),2)
    book.save()
    return render(request,"books/vote.html",{"book":book})