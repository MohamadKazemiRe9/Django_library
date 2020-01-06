from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(verbose_name="نام",max_length=100)
    auther = models.ForeignKey("Author",on_delete=models.CASCADE)

class Author(models.Model):
    fname = models.CharField(verbose_name="نام کوچک نویسنده",max_length=100)
    lname = models.CharField(verbose_name="نام خانوادگی نویسنده",max_length=100)
    birthday = models.DateTimeField(verbose_name="تاریخ تولد")