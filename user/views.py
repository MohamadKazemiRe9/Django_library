from django.shortcuts import render ,HttpResponse
from .models import ExpUser

# Create your views here.
def index (request):
    users = ExpUser.objects.all()
    return HttpResponse(users)
