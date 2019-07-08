
from django.db import models

# Create your models here.
class bookdata(models.Model):
    book_id = models.CharField(max_length=50)
    Book_name = models.CharField(max_length =50)
    Author_name = models.CharField(max_length=20)
    
class studentdata(models.Model):
    Student_name = models.CharField(max_length =50)
    Branch = models.CharField(max_length =50)
    Username = models.CharField(max_length =50)
    password = models.CharField(max_length =50)
 